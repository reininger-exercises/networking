# web server
from socket import *

class WebServer:
    def __init__(self, port=12000):
        self._port = port

    def _createServerSocket(self):
        # Creates and binds a TCP server socket for initiating connections.
        serverSocket = socket(AF_INET, SOCK_STREAM)
        serverSocket.bind(('', self._portNumber))
        return serverSocket
