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
