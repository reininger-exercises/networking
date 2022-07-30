# UDPPingerClient.py
# Sends pings to UDPPingServer and calculates RTT
from socket import *

serverName = 'localhost'
serverPort = 12000
pingCount = 10

with socket(AF_INET, SOCK_DGRAM) as clientSocket:
    for ping in range(1, pingCount + 1):
        pingMessage = f'Ping {pingCount}'
        clientSocket.sendto(pingMessage.encode(), (serverName, serverPort))
