import socket
import sys

try:
	s =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	print ("Socket successfully created")
except socket.error as err:
	print("socket creation fail with error%" %(err))
	
try:
	host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:
	print("there was an error resolving the host")
	sys.exit()
	
s.connect((host_ip, 80))

print("the socket has successfully connected to google")
