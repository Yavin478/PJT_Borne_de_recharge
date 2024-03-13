##############################################################################################
#                                                                                            #
#                                                                                            #
#                                                                                            #
#                                                                                            #
#                                  Tag 166tt, Zt Rezal, KIN 215                              #
#                                                                                            #
#                                                                                            #
#                                                                                            #
#                                                                                            #
##############################################################################################

import RPi.GPIO as GPIO
from time import *
from lcd import *

from pad4pi import rpi_gpio

key_p = ""

GPIO.setwarnings(False)

def get_key():

	GPIO.setmode(GPIO.BCM)
	#GPIO.setwarnings(False)

	KEYPAD = [[1,2,3],[4,5,6],[7,8,9],["*",0,"#"]]
	

	ROW_PINS = [27,22,10,9]
	COL_PINS = [25,11,8,7]

	factory = rpi_gpio.KeypadFactory()

	keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)


	def process_Key(key):
		#print(key)
		global key_p
		key_p = str(key)

	keypad.registerKeyPressHandler(process_Key)
	global key_p
	try:
		while 1:
			#print "key is : " + key_p
			if key_p != "":
				#print "Returning key"
				break
				return key_p
			else:
				sleep(0.25)
	except KeyboardInterrupt:
		#print "Goodbye"
		GPIO.cleanup()
		return ""
	#finally:
	#	GPIO.cleanup()

def read_keyb():
	global key_p
	#print "Getting key"
	key = get_key()
	#print "Got key"
	GPIO.cleanup()
	sel_key = "" + key_p
	key_p = ""
	return sel_key

def sel_mode(keys):
	while 1:
		key = read_keyb()
		if key in keys:
			return key

def type_code(lcd):
	key = sel_mode(["1","2","3","4","5","6","7","8","9","0","*","#"])
	code = ""
	while key != "*":
		if key == "F":
			return False
		elif key == "#":
			code = code[:-1]
			write_line(lcd,code,4)
		else:
			code += key
			write_line(lcd,code,4)
		key = sel_mode(["1","2","3","4","5","6","7","8","9","0","*","#"])
	return code

#print "The key is : " + read_keyb()
#GPIO.cleanup()
