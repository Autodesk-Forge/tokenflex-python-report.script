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

import simple_http_server as SimpleHTTPServer
import consumption_reporting as ConsumptionReporting
from threading import Thread
from time import sleep
import pytest


@pytest.mark.skip()
def shutdownServer():
    sleep(30)
    SimpleHTTPServer.httpd.shutdown()


def testServer():
    thread = Thread(target=shutdownServer)
    thread.start()
    SimpleHTTPServer.startHttpServer()
    thread.join()


def testConsumption():
    ConsumptionReporting.start(None)
