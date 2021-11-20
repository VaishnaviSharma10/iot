import socket

s = socket.socket()
print("socket successfully created")


port = 1238

s.bind(('',port))
print("socket binded to %s" %(port))

s.listen(5)
print("socket is listening")

while True:
	
	c, addr = s.accept()
	print('got connection from ',addr)
	
	c.send('thank you for connecting'.encode())
	c.close()
