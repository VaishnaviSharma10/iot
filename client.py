import socket

s = socket.socket()
s.connect(('127.0.0.1', 1238))

print(s.recv(1024).decode())
s.close()
