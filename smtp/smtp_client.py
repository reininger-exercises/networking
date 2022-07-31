# Skeleton Python Code for the Mail Client
from base64 import *
from socket import *
from ssl import *
from textwrap import wrap

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# load crednetials
with open('credentials.txt', 'r') as credentialFile:
	lines = credentialFile.readlines()
	lines = [line.strip() for line in lines]
	username, password = lines[:2]

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ('smtp.office365.com', 587)

# Create socket called clientSocket and establish a TCP connection with
# mailserver
try:
	clientSocket = socket(AF_INET, SOCK_STREAM)
except:
	exit(1)

clientSocket.connect(mailserver)

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
	print('220 reply not received from server.')
	exit(1)

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '250':
	print('250 reply not received from server.')
	exit(1)

# Send Starttls command
startTlsCommand = 'STARTTLS\r\n'
clientSocket.send(startTlsCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
	print('220 reply not received from server.')
	exit(1)

clientSocket = wrap_socket(clientSocket, ssl_version=PROTOCOL_SSLv23)

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '250':
	print('250 reply not received from server.')
	exit(1)

# authenticate
authLoginCommand = 'AUTH LOGIN\r\n'
clientSocket.send(authLoginCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '334':
	print('334 reply not received from server.')
	exit(1)

# send credentials
clientSocket.send(b64encode(username.encode())+b'\r\n')
recv = clientSocket.recv(1024).decode()
print(recv)
clientSocket.send(b64encode(password.encode())+b'\r\n')
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '235':
	print('235 reply not received from server.')
	exit(1)

# Send MAIL FROM command and print server response.
mailFromCommand = f'MAIL FROM: <{username}>\r\n'
clientSocket.send(mailFromCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '250':
	print('250 reply not received from server.')
	exit(1)

# Send RCPT TO command and print server response.
# Fill in start

# Fill in end

# Send DATA command and print server response.
# Fill in start

# Fill in end

# Send message data.
# Fill in start

# Fill in end

# Message ends with a single period.
# Fill in start

# Fill in end

# Send QUIT command and get server response.
# Fill in start

# Fill in end

