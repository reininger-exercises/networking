# client program
import socket
import sys

ADDRESS = ('localhost', 5000)
BUFFSIZ = 4096

if __name__ == '__main__':
	text = input()
	with  socket.create_connection(ADDRESS) as s:
		s.sendall(text.encode())
		data = s.recv(BUFFSIZ).decode()
	print(data)
		
