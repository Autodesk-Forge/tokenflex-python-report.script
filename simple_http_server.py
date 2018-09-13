import argparse
import json
import requests
import SimpleHTTPServer
import SocketServer
import urlparse

parser = argparse.ArgumentParser(description='Run Forge authentication script.')
parser.add_argument('--FORGE_CLIENT_ID', required=True)
parser.add_argument('--FORGE_CLIENT_SECRET', required=True)
parser.add_argument('--FORGE_CALLBACK_URL', required=True)
args = parser.parse_args()
access_token_url = 'https://developer-stg.api.autodesk.com/authentication/v1/gettoken'

class ForgeCallbackHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        bits = urlparse.urlparse(self.path)
        if bits.path == '/forge/oauth/callback':
            code = bits.query.replace("code=", "")
            data = {
                'client_id': args.FORGE_CLIENT_ID,
                'client_secret': args.FORGE_CLIENT_SECRET,
                'grant_type': 'authorization_code',
                'code': code,
                'redirect_uri': args.FORGE_CALLBACK_URL
            }
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            resp = requests.post(access_token_url, headers=headers, data=data)
            if resp.status_code == 200:
                access_token = resp.json()['access_token']
                print access_token
                

PORT = 3000
httpd = SocketServer.TCPServer(("", PORT), ForgeCallbackHTTPRequestHandler)

print "serving at port", PORT
httpd.serve_forever()