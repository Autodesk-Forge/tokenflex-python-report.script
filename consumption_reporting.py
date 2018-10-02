import argparse
import json
import polling
import requests
import urllib

def downloadCsvFile(download_url, download_filename):
    print 'Downloading CSV file ...'
    resp = requests.get(download_url)
    resp.raise_for_status()
    if resp.status_code == 200:
        open(download_filename, 'wb').write(resp.content)

def getContracts(access_token):
    print 'Getting Contracts ...'
    get_contract_url = base_tokenflex_api + '/v1/contract'
    headers = {'Authorization': 'Bearer ' + access_token}
    resp = requests.get(get_contract_url, headers=headers)
    resp.raise_for_status()
    if resp.status_code == 200:
        return resp.json()

def getExportRequestsDetails(access_token, contract_number, request_key):
    print 'Getting Export Request Details ...'
    export_results_url = base_tokenflex_api + '/v1/export/' + contract_number + '/requests/' + urllib.quote_plus(request_key)
    headers = {'Authorization': 'Bearer ' + access_token}
    resp = requests.get(export_results_url, headers=headers)
    resp.raise_for_status()
    if resp.status_code == 200:
        print resp.text
        return resp.json()

def pollExportRequestDetails(access_token, contract_number, request_key):
    print 'Polling Export Request Details ...'
    export_results_url = base_tokenflex_api + '/v1/export/' + contract_number + '/requests/' + urllib.quote_plus(request_key)
    headers = {'Authorization': 'Bearer ' + access_token}
    web_handle = polling.poll(
        lambda: requests.get(export_results_url, headers=headers).json()['requestStatus'] == 'Download',
        step = 5,
        timeout = 120
    )
    return web_handle

# POST /export/:contract_number/requests
def submitExportRequest(access_token, contract_number):
    print 'Submitting export for contract: ' + contract_number
    export_request_url = base_tokenflex_api + '/v1/export/' + contract_number + '/requests'
    headers = { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token }
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
            "CLOUD_PRODUCT"
        ],
        "where": "contractYear=1",
        "downloadFileName": contract_number + "_myYear1DesktopCloudUsage.csv"
    }
    resp = requests.post(export_request_url, headers=headers, data=json.dumps(payload))
    resp.raise_for_status()
    if resp.status_code == 200:
        return resp.json()

parser = argparse.ArgumentParser(description='Run consumption report.')
parser.add_argument('--FORGE_CLIENT_ID', required=True)
parser.add_argument('--FORGE_CLIENT_SECRET', required=True)
parser.add_argument('--FORGE_CALLBACK_URL', required=True)
args = parser.parse_args()

base_url = 'https://developer.api.autodesk.com'
base_tokenflex_api = 'https://developer.api.autodesk.com/tokenflex'
authorize_url = base_url + '/authentication/v1/authorize'

# Step 1: Direct the user to the authorization web flow
# Since this is a CLI script we do not redirect. In a web application, you would
# redirect the user to the authentication URL below.
authorization_url = authorize_url + '?response_type=code&client_id=' + args.FORGE_CLIENT_ID + '&redirect_uri=' + urllib.quote_plus(args.FORGE_CALLBACK_URL) + '&scope=data:read'
print "Go to the following link in your browser: "
print authorization_url

# Step 2: After the user has granted access to you, an access token has been issued
accepted = 'n'
while accepted.lower() == 'n':
    accepted = raw_input('Have you authorized me? (y/n) ')
    if accepted == 'n':
        quit()
    elif accepted == 'y':
        print 'Access granted!'
        access_token = raw_input('Please enter access token value here: ')
        if access_token != '':
            contracts = getContracts(access_token)
            # Step 3: Submit an Export request
            for contract in contracts:
                print '*** Found contract: ' + contract['contractNumber']
                contract_number = contract['contractNumber']
                export_request = submitExportRequest(access_token, contract_number)
                # Step 4: Poll for request results
                request_key = export_request['requestKey']
                print '*** Submitted export request: ' + request_key
                request_details = getExportRequestsDetails(access_token, contract_number, request_key)
                if request_details == 'Download':
                    request_status = request_details['requestStatus']
                    print '*** Retrieved export status: ' + request_status
                else:
                    poll_status = pollExportRequestDetails(access_token, contract_number, request_key)
                    if poll_status == True:
                        request_details = getExportRequestsDetails(access_token, contract_number, request_key)
                        request_status = request_details['requestStatus']
                        print '*** Retrieved export status: ' + request_status
                        download_url = request_details['downloadUrl']
                        print '*** Download url: ' + download_url
                        download_filename = request_details['downloadFileName']
                        downloadCsvFile(download_url, download_filename)
                        print '*** Downloaded file: ' + download_filename