# web server
from http import server
from socket import *

class WebServer:
    def __init__(self, port=12000):
        self._port = port

    def start(self):
        with self._createServerSocket() as serverSocket:
            serverSocket.listen(1)
            while True:
                self._handleConnection(serverSocket.accept())

    def _createServerSocket(self):
        # Creates and binds a TCP server socket for initiating connections.
        serverSocket = socket(AF_INET, SOCK_STREAM)
        serverSocket.bind(('', self._portNumber))
        return serverSocket
