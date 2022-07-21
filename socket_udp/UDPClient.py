# UDP client
from socket import *

serverName = 'localhost'
serverPort = 12000
messageBufferLen = 2048

with socket(AF_INET, SOCK_DGRAM) as clientSocket:
	message = input('Input lowercase sentence: ')
	clientSocket.sendto(message.encode(), (serverName, serverPort))
	modifiedMessage, serverAddress = clientSocket.recvfrom(messageBufferLen)
	print(modifiedMessage.decode())

