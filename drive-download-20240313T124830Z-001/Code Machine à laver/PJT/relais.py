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

GPIO.setwarnings(False)

def init_relais():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(14, GPIO.OUT)
	GPIO.setup(15, GPIO.OUT)
	GPIO.setup(18, GPIO.OUT)
	GPIO.setup(23, GPIO.OUT)
	return True

def get_pin(relais):
	if relais == 1:
		pin = 14
	elif relais == 2:
		pin = 15
	elif relais == 3:
		pin = 18
	elif relais == 4:
		pin = 23
	else:
		return -1
	return pin

def open_r(relais):
	init_relais()
	pin = get_pin(relais)
	if pin != -1:
		GPIO.output(pin,True)
		return True
	else:
		return False

def close_r(relais):
	init_relais()
	pin = get_pin(relais)
	if pin != -1:
		GPIO.output(pin,False)
		return True
	else:
		return False

def start_m(relais):
	close_r(relais)
	sleep(0.5)
	open_r(relais)

#init_relais()
#for i in range (1,5):
#	print i
#	close_r(i)
#	sleep(0.5)
#	open_r(i)
#print start_m(4)
#print close_r(3)
#GPIO.cleanup()
#start_m(3)
#close_r(3)
