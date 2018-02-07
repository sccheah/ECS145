# two clients connect to server; each client sends letter
# server appends to global str and sends back to client
# '' means client is dropping out; when clients are gone,
# server will print final string

# USAGE: python clnt.py server_addr port_number

import socket, sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # create Internet TCP socket
s.connect((sys.argv[1], int(sys.argv[2])))              # connect to server

while True:
    usr_input = raw_input("Enter a letter: ")           # get letter from user

    s.send(usr_input)                                   # send input to server

    if usr_input == '':                                 # leave loop if get stop signal
        break

    data = s.recv(1024)                                 # receive str from server
    print data

s.close()
