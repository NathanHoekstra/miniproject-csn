import inbreekbot
import socket
import os
from time import localtime, strftime

SAVED_HASH = '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4'

# Initialize socket
HOST = '192.168.42.1'
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
			log_event("connect from: {0}:{1}".format(address[0], str(address[1])))
			reply = 'SERVER_ACK\n'

		elif b'CLIENT_CODE' in data:
			client_data = data.decode()
			client_message, code = client_data.split(':')
			code = code.strip('\n')
			if code == SAVED_HASH:
				reply = 'SERVER_CODE_CORRECT\n'
				log_event("Correct pin was given")
			else:
				reply = 'SERVER_ALARM_NOTIFY\n'
				log_event("Break in detected, wrong pin given")
				inbreekbot.handle()

		else:
			log_event("non-protocol message: {0}".format(data.decode()))
			reply = 'SERVER_NACK\n'

		if not data:
			log_event('client disconnect')
			break
		connect.sendall(str.encode(reply))
	connect.close()

# Check if logfile exists, else create it
def write_or_append():
	if os.path.exists('/Users/nick/miniproject-csn/alarm.log') == True:
		file_mode = 'a'
	else:
		file_mode = 'w'
	return file_mode

# Log server events
def log_event(message):
	file_mode = write_or_append()
	log_file = open('alarm.log', file_mode)
	time_stamp = strftime("%Y-%m-%d %H:%M:%S", localtime())

	event = time_stamp + ': ' + message + '\n'

	log_file.write(event)
# Main loop
while True:

	connect, address = s.accept()
	print('connect from: {0}:{1}'.format(address[0], str(address[1])))

	client_connection(connect)
