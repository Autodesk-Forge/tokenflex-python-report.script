import argparse
import json
import os
import requests
import SimpleHTTPServer
import SocketServer
import urlparse

class ForgeCallbackHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        bits = urlparse.urlparse(self.path)
        if bits.path == '/api/forge/callback/oauth':
            code = bits.query.replace("code=", "")
            data = {
                'client_id': os.environ['FORGE_CLIENT_ID'] if args.FORGE_CLIENT_ID is None else args.FORGE_CLIENT_ID,
                'client_secret': os.environ['FORGE_CLIENT_SECRET'] if args.FORGE_CLIENT_SECRET is None else args.FORGE_CLIENT_SECRET,
                'grant_type': 'authorization_code',
                'code': code,
                'redirect_uri': os.environ['FORGE_CALLBACK_URL'] if args.FORGE_CALLBACK_URL is None else args.FORGE_CALLBACK_URL
            }
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            resp = requests.post(access_token_url, headers=headers, data=data)
            if resp.status_code == 200:
                access_token = resp.json()['access_token']
                self.send_response(200)
                print access_token

def startHttpServer(args, access_token_url):
    PORT = 3000
    httpd = SocketServer.TCPServer(("", PORT), ForgeCallbackHTTPRequestHandler)
    print "serving at port", PORT
    httpd.serve_forever()

parser = argparse.ArgumentParser(description='Run Forge authentication script.')
parser.add_argument('--FORGE_CLIENT_ID', required=False)
parser.add_argument('--FORGE_CLIENT_SECRET', required=False)
parser.add_argument('--FORGE_CALLBACK_URL', required=False)
args = parser.parse_args()
access_token_url = 'https://developer.api.autodesk.com/authentication/v1/gettoken'

startHttpServer(args, access_token_url)
