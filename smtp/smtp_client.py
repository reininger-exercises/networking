# Skeleton Python Code for the Mail Client
from socket import *
from sys import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
destinationEmail = argv[1]

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ('outlook-com.olc.protection.outlook.com.', 25)

# Create socket called clientSocket and establish a TCP connection with
# mailserver
try:
	clientSocket = socket(AF_INET, SOCK_STREAM)
except:
	exit(1)

def terminate():
	clientSocket and clientSocket.close()
	exit(1)

clientSocket.connect(mailserver)

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
	print('220 reply not received from server.')
	terminate()

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '250':
	print('250 reply not received from server.')
	terminate()


# Send MAIL FROM command and print server response.
mailFromCommand = f'MAIL FROM: <sender@test.com>\r\n'
clientSocket.send(mailFromCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '250':
	print('250 reply not received from server.')
	terminate()

# Send RCPT TO command and print server response.
rcptToCommand = f'RCPT TO: <{destinationEmail}>\r\n'
clientSocket.send(rcptToCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '250':
	print('250 reply not received from server.')
	terminate()

# Send DATA command and print server response.
dataCommand = f'DATA\r\n'
clientSocket.send(dataCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '354':
	print('354 reply not received from server.')
	terminate()

# Send message data.
clientSocket.send(msg.encode())

# Message ends with a single period.
clientSocket.send(endmsg.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '250':
	print('250 reply not received from server.')
	terminate()

# Send QUIT command and get server response.
quitCommand = f'QUIT\r\n'
clientSocket.send(quitCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '221':
	print('221 reply not received from server.')
	terminate()

terminate()
