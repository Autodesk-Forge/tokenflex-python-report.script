import argparse
import json
import os
import requests
import SimpleHTTPServer
import SocketServer
import sys
import urlparse
import config.state as state
import config.env as env
import consumption_reporting as ConsumptionReporting
import urlparse
import BaseHTTPServer

httpd = None


class ForgeCallbackHTTPRequestHandler(
        SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        global httpd
        bits = urlparse.urlparse(self.path)
        if bits.path == urlparse.urlparse(state.args.FORGE_CALLBACK_URL).path:
            state.code = bits.query.replace("code=", "")
            data = {
                'client_id': os.getenv(
                    'FORGE_CLIENT_ID',
                    state.args.FORGE_CLIENT_ID),
                'client_secret': os.getenv(
                    'FORGE_CLIENT_SECRET',
                    state.args.FORGE_CLIENT_SECRET),
                'grant_type': 'authorization_code',
                'code': state.code,
                'redirect_uri': os.getenv(
                    'FORGE_CALLBACK_URL',
                    state.args.FORGE_CALLBACK_URL)}
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            resp = requests.post(
                env.access_token_url,
                headers=headers,
                data=data)
            if resp.status_code == 200:
                state.token = resp.json()['access_token']
                print state.token
                self.send_response(200)
                try:
                    ConsumptionReporting.start(state.token)
                    self.send_response(200)
                except BaseException:
                    print BaseException
                    self.send_response(500)
                httpd.shutdown()


class ThreadingHTTPServer(
        SocketServer.ThreadingMixIn,
        BaseHTTPServer.HTTPServer):
    allow_reuse_address = True


def startHttpServer():
    global httpd
    PORT = 4000
    httpd = ThreadingHTTPServer(
        ("", PORT), ForgeCallbackHTTPRequestHandler)
    print "serving at port", PORT
    httpd.serve_forever()
