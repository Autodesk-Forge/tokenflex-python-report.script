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
    thread = Thread(target = shutdownServer)
    thread.start()
    SimpleHTTPServer.startHttpServer()
    thread.join()

def testConsumption():
    ConsumptionReporting.start(None)
