# two clients connect to server; each client sends letter
# server appends to global str and sends back to client
# '' means client is dropping out; when clients are gone,
# server will print final string

# USAGE: python srvr.py port_number

import sys, socket, thread

# standard communication between threads is via globals

# function for thread to serve particular client
def serveclient(c):
    global v, nclnt, vlock, nclntlock

    while True:
        k = c.recv(1)               # receive letter from client

        if k == '':
            break

        # concat v with k in atomic manner, i.e. w/ protection by locks
        vlock.acquire()
        v += k
        vlock.release()

        # send new v back to client
        c.send(v)

    c.close()
    nclntlock.acquire()
    nclnt -= 1
    nclntlock.release()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       # set up Internet TCP socket
s.bind(('', int(sys.argv[1])))
s.listen(5)

v = ''                                              # concatenated string
vlock = thread.allocate_lock()                      # set up lock to guard v

nclnt = 2                                           # number of clients
nclntlock = thread.allocate_lock()                  # set up lock to guard nclnt

for i in range(nclnt):
    clnt, ap = s.accept()         # wait for call, get new socket to use for this client

    # start new thread for this client w/ serveclient() as thread's function, w/
    # parameter clnt; not that parameter set must be a tuple; in this case, tuple
    # is of length 1, so a comma is needed
    thread.start_new_thread(serveclient, (clnt,))

# shut down listening socket since it isnt needed anymore
s.close()

# wait for both threads to finish
while nclnt > 0:
    pass

print 'The final value of v is', v
