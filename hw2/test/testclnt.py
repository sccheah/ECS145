import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1], int(sys.argv[2])))

string = "hello thar"

s.sendall(str(sys.getsizeof(string)))
s.sendall(string)
