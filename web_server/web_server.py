# web server
from pathlib import Path
from socket import *
import signal
import sys

from numpy import spacing

class WebServer:
    def __init__(self, port=12000):
        self._port = port
        self._bufLen = 2048
        self._registerSignalHandlers()

    def _registerSignalHandlers(self):
        signal.signal(signal.SIGINT, self._signal_handler)

    def _signal_handler(self, sig, frame):
        print('\nProcess received signal: ', signal.strsignal(sig))
        print('\nShutting down...')
        sys.exit(0)

    def start(self):
        # Starts web server process.
        with self._createServerSocket() as serverSocket:
            print('ready to accept connections')
            serverSocket.listen(1)
            while True:
                self._handleConnection(*serverSocket.accept())

    def _createServerSocket(self):
        # Creates and binds a TCP server socket for initiating connections.
        serverSocket = socket(AF_INET, SOCK_STREAM)
        serverSocket.bind(('', self._port))
        return serverSocket

    def _handleConnection(self, connectionSocket, address):
        # Handles communication once a connection is accepted.
        with connectionSocket:
            print(f'connected to: address={address[0]} port={address[1]}')
            message = connectionSocket.recv(self._bufLen)
            message = message.decode()
            print('Message:\n', message, sep='')
            response = self._handleRequest(message)
            connectionSocket.send(response.encode())

        print(f'connection to {address} closed')

    def _handleRequest(self, request: str):
        # Handles a received request.
        lines = request.split(sep='\r\n')
        requestLineTokens = lines[0].split()
        if not self.isValidRequestLine(requestLineTokens):
            return 'HTTP/1.1 400 Bad Request\r\n'
            
        requestPath = requestLineTokens[1][1:]
        if not self.isAuthorizedPath(requestPath):
            return 'HTTP/1.1 403 Not Authorized\r\n'

        path = Path.cwd() / requestPath
        if not path.exists():
            return 'HTTP/1.1 404 Not found\r\n'
        else:
            return 'HTTP/1.1 200 OK\r\n\r\n' + open(path).read()

    def isValidRequestLine(self, tokens):
        if len(tokens) != 3:
            return False
        method, resource, protocol = tokens
        if method != 'GET':
            return False
        if protocol[:4] != 'HTTP':
            return False
        return True

    def isAuthorizedPath(self, path):
        segments = path.split('/')
        authorized = all(segment not in ['..', '~'] for segment in segments)
        return authorized
