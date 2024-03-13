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

import datetime
import time

def get_hour():
	now = datetime.datetime.now()
	#print now.hour
	h = str(now.hour)
	if len(h) == 1:
		return "0" + h
	else:
		return h

def get_min():
	now = datetime.datetime.now()
	#print now.minute
	m = str(now.minute)
	if len(m) == 1:
		return "0" + m
	else:
		return m

def get_code():
	return get_hour() + get_min()

def get_timestamp():
	return int(time.time())

def get_delta(t1,t2):
	return t2-t1

#print get_hour()
#print get_min()
#t1 = get_timestamp()
#time.sleep(5)
#t2 = get_timestamp()
#print get_delta(t1,t2)
