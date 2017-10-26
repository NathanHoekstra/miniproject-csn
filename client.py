#!/usr/bin/python3

# add library's
import RPi.GPIO as GPIO
import time
import socket
import hashlib

# Setup server ip and port
host = '192.168.42.1'
port = 1337

# Create variable s for socket library
s = socket.socket()
s.connect((host, port))

# Set GPIO mode to use broadcom pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

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

# This function handles the interaction with the keypad
def keypad():
	# Create list to store key presses
	list = []
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
			time.sleep(0.2)
			break

	#convert list to string and hash the code with sha256
	string = ''.join(str(e) for e in list)
	string = string.encode()
	hashed_string = hashlib.sha256(string).hexdigest()
	code = 'CLIENT_CODE:' + hashed_string
	return code

# ---- Create functions to turn off/on led's ----

# Turn Blue led on (Input control led)
def bled_on():
	GPIO.output(16, GPIO.HIGH)

# Turn Blue led off (Input control led)
def bled_off():
	GPIO.output(16, GPIO.LOW)

# Turn Red led on (Disarmed led)
def rled_on():
	GPIO.output(20, GPIO.HIGH)

# Turn led led off (Disarmed led)
def rled_off():
	GPIO.output(20, GPIO.LOW)

# Turn green led on (Armed led)
def gled_on():
	GPIO.output(21, GPIO.HIGH)

# Turn green led off (Armed led)
def gled_off():
	GPIO.output(21, GPIO.LOW)

# Function to handle the data to be send
def send_data(data):
	s.send(data.encode())
	data = s.recv(1024).decode()
	return data


# Set state of alarm
alarm_state = False

# Turn off led's before use
bled_off()
gled_off()
rled_off()

# While loop for all the main logic
while True:
	# Check for actual status of confirm button
	button_confirm = GPIO.input(23)
	# Start with empty data string (just in case)
	data = ''
	# Check if button is being pressed
	if button_confirm == False:
		time.sleep(0.2) # sleep for 200 miliseconds to prevent doubble press
		print('--- Type keycode now! ---')
		# Turn on blue led to notify user that they can type the code
		bled_on()
		# Call the keypad function place return value in message
		message = keypad()
		print(message)
		# Turn off blue led
		bled_off()
		# Send data to server and place response in data variable
		data = send_data(message)
		# Print the response of the server
		print('Status code: {}'.format(data))
	# Check if SERVER_CODE_CORRECT exists in data == keycode is correct
	if 'SERVER_CODE_CORRECT' in data:
		# If the alarm state is false, turn the alarm on and turn the green led on
		if alarm_state == False:
			gled_on()
			rled_off()
			alarm_state = True
		# If the alarm state is true, turn the alarm off and turn the red led on
		elif alarm_state == True:
			gled_off()
			rled_on()
			alarm_state = False
	# If the keycode is incorrect:
	elif 'SERVER_ALARM_NOTIFY' in data:
		# Blink 3 times
		for i in range(3):
			rled_on()
			time.sleep(0.5)
			rled_off()
			time.sleep(0.5)

s.close()
