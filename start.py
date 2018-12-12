#####################################################################
## Copyright (c) Autodesk, Inc. All rights reserved
## Written by Forge Partner Development
##
## Permission to use, copy, modify, and distribute this software in
## object code form for any purpose and without fee is hereby granted,
## provided that the above copyright notice appears in all copies and
## that both that copyright notice and the limited warranty and
## restricted rights notice below appear in all supporting
## documentation.
##
## AUTODESK PROVIDES THIS PROGRAM "AS IS" AND WITH ALL FAULTS.
## AUTODESK SPECIFICALLY DISCLAIMS ANY IMPLIED WARRANTY OF
## MERCHANTABILITY OR FITNESS FOR A PARTICULAR USE.  AUTODESK, INC.
## DOES NOT WARRANT THAT THE OPERATION OF THE PROGRAM WILL BE
## UNINTERRUPTED OR ERROR FREE.
#####################################################################

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
        '&scope=data:read%20data:write')
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
