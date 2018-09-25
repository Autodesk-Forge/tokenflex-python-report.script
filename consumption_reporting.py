import argparse
import json
import requests
import urllib

def getContracts(access_token):
    get_contract_url = base_tokenflex_api + '/v1/contract'
    headers = {'Authorization': 'Bearer ' + access_token}
    resp = requests.get(get_contract_url, headers=headers)
    resp.raise_for_status()
    if resp.status_code == 200:
        print 'Getting Contracts ...'
        print resp.text
        return resp.json()

# POST /export/:contract_number/requests
def submitExportRequest(access_token, contract_number):
    print 'Requesting export for contract: ' + contract_number
    export_request_url = base_tokenflex_api + '/v1/export/' + contract_number + '/requests'
    headers = { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token }
    payload = {
        "fields": [
            "contractYear",
            "chargedItemID",
            "tokenPool",
            "reasonType",
            "reasonComment",
            "usageCategory",
            "usageDate",
            "transactionDate",
            "productLineCode",
            "productName"
        ],
        "metrics": [
            "tokensConsumed",
            "quantity"
        ],
        "usageCategory": [
            "MANUAL_ADJUSTMENT",
            "MANUAL_CONSUMPTION"
        ],
        "where": "contractYear=1",
        "downloadFileName": "myYear1Adjustments.csv"
    }
    resp = requests.post(export_request_url, headers=headers, data=json.dumps(payload))
    resp.raise_for_status()
    if resp.status_code == 200:
        print resp.text

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
        print 'accepted: ', accepted
    elif accepted == 'y':
        print 'Access granted!'
        access_token = raw_input('Please enter access token value here: ')
        if access_token != '':
            contracts = getContracts(access_token)
            # Step 3: Submit an Export request
            for contract in contracts:
                contract_number = contract['contractNumber']
                submitExportRequest(access_token, contract_number)