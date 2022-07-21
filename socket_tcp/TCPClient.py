# TCP client
from socket import *

serverName = 'localhost'
serverPort = 12000
messageBufferLen = 2048

with socket(AF_INET, SOCK_STREAM) as clientSocket:
	clientSocket.connect((serverName, serverPort))
	message = input('Input lowercase sentence: ')
	clientSocket.send(message.encode())
	modifiedMessage = clientSocket.recv(messageBufferLen)
	print('From Server: ', modifiedMessage.decode())

