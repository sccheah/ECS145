# simple illustration of nonblocking sockets

# two clients connect to server; each client repeatedly sends letters
# server then appends to global str and reports the str to client
# empty str from client means it is dropping out
# when all clients are gone, it prints out final str

# USAGE: python strclnt.py server_address port_num

import sys, socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1], int(sys.argv[2])))

while True:
    usr_input = raw_input("Enter a letter: ")
    s.send(usr_input)

    if usr_input == '':
        break

    data = s.recv(1024)
    print data

s.close()
