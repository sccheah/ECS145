# mult clients connect to server; each client keeps sending letter
# server concats to global str and sends str back to client
# client sends '' when dropping out

# USAGE: python strsvr.py port_num

import socket, sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # create a listening socket
s.bind(('', int(sys.argv[1])))          # bind host with port number

s.listen(5)             # allow up to 5 pending connections

string = ''             # global str to hold string
client_socket_list = [] # list of all connected sockets

num_client = 2          # statically make sure we only have 2 clients

# must have two clients. could make listen socket as nonblocking. mac wont let me.
# alternative is using threads.
for i in range(num_client):
    conn, addr = s.accept()
    conn.setblocking(0)         # sets connected socket as non-blocking
    client_socket_list.append(conn)         # append this connection to a list


while len(client_socket_list) > 0:
    conn = client_socket_list.pop(0)        # remove first conn socket from list
    client_socket_list.append(conn)         # put conn socket back into list

    try:
        letter = conn.recv(1)   # accept one byte

        if letter == '':
            conn.close()
            client_socket_list.remove(conn)

        string += letter
        conn.send(string)

    except:
        continue

s.close()
print 'The final value of string is', string
