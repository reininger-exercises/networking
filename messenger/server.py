# server
from socket import *

serverPort = 12000
bufLen = 2048

with socket(AF_INET, SOCK_STREAM) as serverSocket:
	serverSocket.bind(('', serverPort))
	serverSocket.listen(1)
	while True:
		connectionSocket, address = serverSocket.accept()
		with connectionSocket:
			message = connectionSocket.recv(bufLen).decode()
			print(message)

