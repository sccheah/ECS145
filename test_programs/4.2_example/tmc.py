# client/server pair; client program sends string to server; this is CLIENT
# server echoes back to client (multiple copies) and prints to screen

import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # create socket

host = sys.argv[1]
port = int(sys.argv[2])

s.connect((host, port))     # connect with server

s.send(sys.argv[3])         # send data to server

while True:                 # loop to keep receiving data from server
    data = s.recv(1000)     # receive up to 1000 bytes at a time
                            # blocks til receives data
            # when entire message received from server, recv() will return empty string

    if data == '':            # if done receiving entire message, break
        break

    print data              # print data from server

    print 'received', len(data), 'bytes'

s.close()                   # close the socket
