# client
from socket import *

serverName = 'localhost'
serverPort = 12000
bufLen = 2048

with socket(AF_INET, SOCK_STREAM) as clientSocket:
	clientSocket.connect((serverName, serverPort))
	while True:
		message = input('message: ')
		clientSocket.send(message.encode())

