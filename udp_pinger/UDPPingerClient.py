# UDPPingerClient.py
# Sends pings to UDPPingServer and calculates RTT
from socket import *
from time import time

serverName = 'localhost'
serverPort = 12000
pingCount = 10
socketTimeout_s = 1
MILLISECONDS_PER_SECOND = 1000

with socket(AF_INET, SOCK_DGRAM) as clientSocket:
    clientSocket.settimeout(socketTimeout_s)
    for ping in range(1, pingCount + 1):
        pingMessage = f'Ping {ping}'
        txTime_s = time()
        clientSocket.sendto(pingMessage.encode(), (serverName, serverPort))
        try:
            message, address = clientSocket.recvfrom(2048)
        except:
            message, address = None, None

        rxTime_s = time()
        rttTime_ms = MILLISECONDS_PER_SECOND * (rxTime_s - txTime_s)

        print(
            f'Tx: {pingMessage} RTT(ms): '\
            f'{f"{rttTime_ms:.3f}" if address else "*" * 5} '\
            f'Rx: {message and message.decode() or ""}'
        )
