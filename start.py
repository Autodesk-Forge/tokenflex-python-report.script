#!/usr/bin/env python2.7
import argparse
import config.state as state
import config.env as env
import urllib
import simple_http_server as SimpleHTTPServer
from urlparse import urljoin


def start():
    parser = argparse.ArgumentParser(
        description='Run Forge authentication script.')
    parser.add_argument('--FORGE_CLIENT_ID', required=True)
    parser.add_argument('--FORGE_CLIENT_SECRET', required=True)
    parser.add_argument('--FORGE_CALLBACK_URL', required=True)
    state.args = parser.parse_args()
    authorization_url = urljoin(
        env.authorize_url,
        '?response_type=code&client_id=' +
        state.args.FORGE_CLIENT_ID +
        '&redirect_uri=' +
        urllib.quote_plus(
            state.args.FORGE_CALLBACK_URL) +
        '&scope=data:read')
    try:
        import webbrowser
        webbrowser.open(authorization_url, new=0, autoraise=True)
    except ImportError:
        print "Can not import webbrowser"
    print "Go to the following link in your browser if the redirection hasn't started: "
    print authorization_url
    SimpleHTTPServer.startHttpServer()


if __name__ == "__main__":
    start()
