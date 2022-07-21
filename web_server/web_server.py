# web server
from socket import *

class WebServer:
    def __init__(self, port=12000):
        self._portNumber = port
