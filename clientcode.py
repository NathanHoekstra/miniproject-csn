import socket
import hashlib

host = '145.89.106.170'
port = 1337

s = socket.socket()
s.connect((host, port))

#def buttons():

message = input('Voer een vier cijferige code in')

while message != 'q':
    s.send(message.encode())
    data = s.recv(1024).decode()

    print('Status code' + data)

    message = input('Voer een bericht in')

s.close()

