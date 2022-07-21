# UDP server
from socket import *

serverPort = 12000
msgBufferSize = 2048

with socket(AF_INET, SOCK_DGRAM) as serverSocket:
	serverSocket.bind(('', serverPort))
	print('The server is ready to receive')
	while True:
		message, clientAddress = serverSocket.recvfrom(msgBufferSize)
		modifiedMessage = message.decode().upper()
		serverSocket.sendto(modifiedMessage.encode(), clientAddress)

