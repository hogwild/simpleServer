import socket

s = socket.socket()
host = socket.gethostname()
port = 1234

s.connect((host, port))
print(s.recv(1024).decode('utf-8'))
# in Python3 the socket.socket.send method only can send bytes type data 
