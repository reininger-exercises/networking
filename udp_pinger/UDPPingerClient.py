# UDPPingerClient.py
# Sends pings to UDPPingServer and calculates RTT
from socket import *

serverName = 'localhost'
serverPort = 12000
pingCount = 10
socketTimeoutSeconds = 1

with socket(AF_INET, SOCK_DGRAM) as clientSocket:
    clientSocket.settimeout(socketTimeoutSeconds)
    for ping in range(1, pingCount + 1):
        pingMessage = f'Ping {ping}'
        clientSocket.sendto(pingMessage.encode(), (serverName, serverPort))
        try:
            message, address = clientSocket.recvfrom(2048)
            print('server responded with: ', message.decode())
        except:
            print('Ping timed out')
