import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', int(sys.argv[1])))
s.listen(5)

conn, addr = s.accept()
numBytes = conn.recv(1024)
instructions = conn.recv(int(numBytes))

print numBytes
print instructions
