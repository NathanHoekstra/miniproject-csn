import socket
from os import *

# Initialize socket
HOST = 'localhost'
PORT = 1337
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.bind((HOST, PORT)) # Bind socket to localhost:1337
except socket.error as e:
	print('Something went wrong while trying to bind port: {}'.format(str(e)))

s.listen(5)

# Handling client connection
def client_connection(connect):

	while True:
		data = connect.recv(1024)
		if data == b'CLIENT_HELLO\n':
			reply = 'SERVER_ACK\n'
		elif data == b'CLIENT_ALARM\n':
			print('SOME ASSHOLE CAM INTO THE HOUSE!!')
			reply = 'SERVER_ALARM_NOTIFY\n'
		else:
			reply = 'SERVER_NACK\n'
		if not data:
			print('client disconnect')
			break
		connect.sendall(str.encode(reply))
	connect.close()

# Main loop
while True:

	connect, address = s.accept()
	print('connect from: {0}:{1}'.format(address[0], str(address[1])))

	client_connection(connect)
