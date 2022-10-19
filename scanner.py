#!/bin/python

import sys
import socket
from datetime import datetime

#Define our target 
if len(sys.argv) == 2 :
	target = socket.gethostbyname(sys.argv[1])
else : 
	print("Invalid number of arguments")
	print("Syntax: python3 scanner.py <ip>")

#Add a pretty banner
print("-" * 50)
print("Scanning Target" + target)
print("Time Started" + str(datetime.now()))
print("-" * 50)

try:
	for port in range(1,65535) : 
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		if result ==0:
			print("Port {} is open".format(port))
		s.close()
except KeyboardInterrupt:
	print("\n Exiting Program")
	sys.exit()
	
except socket.gaierror:
	print("Hostname could not be resolved")
	sys.exit()
	
except socket.error:
	print("Could not connect to server.")
	sys.exit()	
				
			
	 
