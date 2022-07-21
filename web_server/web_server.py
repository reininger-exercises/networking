# web server
from socket import *
import signal
import sys

class WebServer:
    def __init__(self, port=12000):
        self._port = port
        self._bufLen = 2048
        self._registerSignalHandlers()

    @property
    def bufLen(self):
        # Length of max segment size received from client at a time in bytes
        return self._bufLen

    @bufLen.setter
    def bufLen(self, newBufLen):
        self._bufLen = max(0, newBufLen)

    def _registerSignalHandlers(self):
        signal.signal(signal.SIGINT, self._signal_handler)

    def _signal_handler(slef, sig, frame):
        print('\nShutting down...')
        sys.exit(0)

    def start(self):
        with self._createServerSocket() as serverSocket:
            print('Ready to accept connections')
            serverSocket.listen(1)
            while True:
                self._handleConnection(*serverSocket.accept())

    def _createServerSocket(self):
        # Creates and binds a TCP server socket for initiating connections.
        serverSocket = socket(AF_INET, SOCK_STREAM)
        serverSocket.bind(('', self._port))
        return serverSocket

    def _handleConnection(self, connectionSocket, address):
        with connectionSocket:
            print('Server connected to: ', address)
            message = connectionSocket.recv(self.bufLen).decode()
            print('Message: ', message)
        print(f'Connection to {address} closed')

    def _handleRequest(self, request):
        pass