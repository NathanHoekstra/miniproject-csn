#!/usr/bin/python3

# add library's
import RPi.GPIO as GPIO
import time
import socket
import hashlib

# Setup server ip and port
host = '145.89.106.170'
port = 1337

s = socket.socket()
s.connect((host, port))

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Setup list and string to store passcode
list = []

# Define led outputs
GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)

# Define keypad inputs
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(5,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(6,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23,GPIO.IN, pull_up_down=GPIO.PUD_UP)

def keypad():
  # Create empty string before use
  string = ''
  while True:
  	button_01 = GPIO.input(4)
  	button_02 = GPIO.input(17)
  	button_03 = GPIO.input(27)
  	button_04 = GPIO.input(22)
  	button_05 = GPIO.input(5)
  	button_06 = GPIO.input(6)
  	button_07 = GPIO.input(13)
  	button_08 = GPIO.input(19)
  	button_09 = GPIO.input(26)
  	button_confirm = GPIO.input(23)

  	if button_01 == False:
  		print('Button 1 pressed')
  		list.append(1)
  		time.sleep(0.2)

  	if button_02 == False:
  		print('Button 2 pressed')
  		list.append(2)
  		time.sleep(0.2)

  	if button_03 == False:
  		print('Button 3 pressed')
  		list.append(3)
  		time.sleep(0.2)

  	if button_04 == False:
  		print('Button 4 pressed')
  		list.append(4)
  		time.sleep(0.2)

  	if button_05 == False:
  		print('Button 5 pressed')
  		list.append(5)
  		time.sleep(0.2)

  	if button_06 == False:
  		print('Button 6 pressed')
  		list.append(6)
  		time.sleep(0.2)

  	if button_07 == False:
  		print('Button 7 pressed')
  		list.append(7)
  		time.sleep(0.2)

  	if button_08 == False:
  		print('Button 8 pressed')
  		list.append(8)
  		time.sleep(0.2)

  	if button_09 == False:
  		print('Button 9 pressed')
  		list.append(9)
  		time.sleep(0.2)

  	if button_confirm == False:
  		print('Confirm pressed')
  		break

  #convert list to string and print to terminal
  string = 'CLIENT_CODE:' + ''.join(str(e) for e in list)
  print('De ingevoerde code is: {}'.format(string))
  return string


message = keypad()
message = message + '\n'
print(message)
s.send(message.encode())
data = s.recv(1024).decode()

print('Status code: ' + data)

s.close()

