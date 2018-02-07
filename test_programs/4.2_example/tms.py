# simple client/server pair; this is the SERVER
# client sends string to server, server echoes back to client in multiple copies
# client then prints to screen

import socket       # contains all comm methods we need
import sys

# create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = int(sys.argv[1])
s.bind(('', port))      # reserve port to current ip addr

s.listen(5)             # listening socket to allow 5 pending conn req at a time

conn, addr = s.accept()         # tells OS to BLOCK til connection req (client calls connect())
                                # sets up a connected socket to comm w/ client
print 'client is at ', addr

data = conn.recv(1000000)       # read data from connected socket 
data = 10000 * data

conn.send(data)
conn.close()
