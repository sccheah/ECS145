# simple client/server pair; this is the SERVER
# client sends string to server, server echoes back to client in multiple copies
# client then prints to screen

import socket
import sys

#create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# associate the socket with a post
host = '' # can leave this blank on server side
port = int(sys.argv[1])
s.bind((host, port)) # send as a tuple?

# accept "call" from client
s.listen(1)

# tells OS to wait for connection request. Block until req comes in from client
# at a remote machine. Occurs when client executes s.connect((host, port))
conn, addr = s.accept()
print "client is at", addr

# read string from client (assumed short, so one call to recv() is good)
# make multiple copies (show need for while loop on client side)

data = conn.recv(10000000)
data = 10000 * data # concatenate data within itself 999 times

# wait for go-ahead signal from keyboard (demo that recv() at the client will block til server sends)

z = raw_input()

# send data
conn.send(data)

#close connection
conn.close()
