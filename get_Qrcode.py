#Ylan a réglé le problème dans un de ses codes en utilisant la fonction get_qrcode de Tag 166tt.
from inputimeout import inputimeout, TimeoutOccurred

def get_qrcode():
	try:
		tmp = inputimeout(timeout=20)
	except TimeoutOccurred:
		return False
	while tmp[0] != '[' and tmp[-1] != ']':
		try:
			tmp = inputimeout(timeout=20)
		except TimeoutOccurred:
			return False
	return tmp

#print get_qrcode()
#qrcode=get_qrcode()

import serial
import time  # Optional (if using time.sleep() below)

connected = False
port = 'COM10'
baud = 9600

try:
	print('Port.......' + port)
	print('Baudrate...' + str(baud))
	ser = serial.Serial(port, baud, timeout=0)

	while (True):
		# NB: for PySerial v3.0 or later, use property `in_waiting` instead of function `inWaiting()` below!
		if (ser.inWaiting() > 0):  # if incoming bytes are waiting to be read from the serial input buffer
			data_str = ser.read(ser.inWaiting()).decode(
				'ascii')  # read the bytes and convert from binary array to ASCII
			print(data_str,
				  end='')  # print the incoming string without putting a new-line ('\n') automatically after every print()
		# Put the rest of your code you want here
		time.sleep(
			0.01)  # Optional: sleep 10 ms (0.01 sec) once per loop to let other threads on your PC run during this time.
except:
	print('Error ' + port + ' is not connected')
