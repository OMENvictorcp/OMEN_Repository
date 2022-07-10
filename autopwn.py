#!/bin/python3 

import requests
import pdb
import sys
import signal
import threading
import time


#ctrl+c


def def_handler(sig, frame):
	print ("\n Saliendo...\n")
	sys.exit(1)

#variables globale
main_url = "http://10.10.10.27/admin.php"
		
def makeRequest():
	
	headers = {
	    'Cookie': 'adminpowa=noonecares'
	r = requests.get(main_url +)
}


signal.signal(signal.SIGINT, def_handler)

if __name__ == '__main__':
	time.sleep(5)
