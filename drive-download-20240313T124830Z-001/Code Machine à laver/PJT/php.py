##############################################################################################
#																							#
#																							#
#																							#
#																							#
#								  Tag 166tt, Zt Rezal, KIN 215							  #
#																							#
#																							#
#																							#
#																							#
##############################################################################################

import urllib.parse
import traceback
import sys
import urllib.request as urllib2

def post_value(data,id):
	#print id
	#try:
	#	exc_info = sys.exc_info()
	#	try:
	#		mydata = [('paymentData',str(data))]
	#		mydata = urllib.urlencode(mydata)
	#		path = 'http://localhost/qrcode_curlopt.php'
	#		#path = 'http://localhost/test.php'
	#		req = urllib2.Request(path, mydata)
	#		page = urllib2.urlopen(req).read()
	#		#print page
	#	except urllib2.HTTPError:
	#		return False
	#finally:
	#	traceback.print_exception(*exc_info)
	#	del exc_info

	#mydata = [('paymentData',str(data)),('id',str(id))]
	mydata = dict(paymentData=str(data), id=str(id))
	mydata = urllib.parse.urlencode(mydata).encode("utf-8")
	path = 'http://localhost/qrcode_curlopt.php'
	#path = 'http://localhost/test.php'
	req = urllib2.Request(path, mydata)
	page = urllib2.urlopen(req).read()
	print(page)

#post_value("plop")
