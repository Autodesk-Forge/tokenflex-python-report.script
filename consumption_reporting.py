import argparse
import json
import os
import polling
import requests
import sys
import urllib
import config.env as env
from urlparse import urljoin


def getRespJson(url, access_token):
    headers = {'Authorization': 'Bearer ' + access_token}
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    if resp.status_code == 200:
        return resp.json()


def downloadCsvFile(download_url, download_filename):
    print 'Downloading CSV file ...'
    resp = requests.get(download_url)
    resp.raise_for_status()
    if resp.status_code == 200:
        open(download_filename, 'wb').write(resp.content)


def getContracts(access_token):
    print 'Getting Contracts ...'
    return getRespJson(
        urljoin(
            env.base_tokenflex_api,
            'v1/contract'),
        access_token)


def getExportRequestsDetails(access_token, contract_number, request_key):
    print 'Getting Export Request Details ...'
    return getRespJson(
        urljoin(
            env.base_tokenflex_api,
            'v1/export/' +
            contract_number +
            '/requests/' +
            urllib.quote_plus(request_key)),
        access_token)


def pollExportRequestDetails(access_token, contract_number, request_key):
    print 'Polling Export Request Details ...'
    export_results_url = urljoin(
        env.base_tokenflex_api,
        'v1/export/' +
        contract_number +
        '/requests/' +
        urllib.quote_plus(request_key))
    headers = {'Authorization': 'Bearer ' + access_token}
    web_handle = polling.poll(
        lambda: requests.get(
            export_results_url,
            headers=headers).json(),
        step=5,
        check_success=check_success,
        timeout=1200)
    return web_handle


def check_success(response):
    if response['requestStatus'] == 'Error':
        raise Exception('Download request failed!')
    print 'Response Status: ' + response['requestStatus']
    return 'downloadUrl' in response


def submitExportRequest(access_token, contract_number):
    print 'Submitting export for contract: ' + contract_number
    export_request_url = urljoin(
        env.base_tokenflex_api,
        'v1/export/' +
        contract_number +
        '/requests')
    headers = {'Content-Type': 'application/json',
               'Authorization': 'Bearer ' + access_token}
    payload = {
        "fields": [
            "contractYear",
            "tokenPool",
            "usageCategory",
            "usageDate",
            "productLineCode",
            "productName"
        ],
        "metrics": [
            "tokensConsumed"
        ],
        "usageCategory": [
            "DESKTOP_PRODUCT",
            "CLOUD_PRODUCT",
            "CLOUD_SERVICE"
        ],
        "where": "contractYear=1",
        "downloadFileName": contract_number + "_myYear1DesktopCloudUsage.csv"
    }
    resp = requests.post(
        export_request_url,
        headers=headers,
        data=json.dumps(payload))
    resp.raise_for_status()
    if resp.status_code == 200:
        return resp.json()


def start(access_token):
    if access_token:  # consider using regex to validate the token
        contracts = getContracts(access_token)
        # Submit an Export request
        for contract in contracts:
            print '*** Found contract: ' + contract['contractNumber']
            contract_number = contract['contractNumber']
            export_request = submitExportRequest(access_token, contract_number)
            # Poll for request results
            request_key = export_request['requestKey']
            print '*** Submitted export request: ' + request_key
            request_details = getExportRequestsDetails(
                access_token, contract_number, request_key)
            if request_details == 'Download':
                request_status = request_details['requestStatus']
                print '*** Retrieved export status: ' + request_status
            else:
                poll_status = pollExportRequestDetails(
                    access_token, contract_number, request_key)
                if poll_status:
                    request_details = getExportRequestsDetails(
                        access_token, contract_number, request_key)
                    request_status = request_details['requestStatus']
                    print '*** Retrieved export status: ' + request_status
                else:
                    raise Exception('Error occurred!')
            download_url = request_details['downloadUrl']
            print '*** Download url: ' + download_url
            download_filename = request_details['downloadFileName']
            downloadCsvFile(download_url, download_filename)
            print '*** Downloaded file: ' + download_filename
    else:
        print 'Invalid access_token. Exiting!'
