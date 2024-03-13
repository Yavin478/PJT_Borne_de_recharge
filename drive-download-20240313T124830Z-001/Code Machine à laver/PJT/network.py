import urllib.request as urllib2
import ssl

def internet_on():
	try:
		ssl._create_default_https_context = ssl._create_unverified_context
		urllib2.urlopen('https://lydia-app.com', timeout=5)
		return True
	except urllib2.URLError as err: 
		return False
