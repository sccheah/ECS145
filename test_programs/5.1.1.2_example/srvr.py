# two clients connect to server; each client sends letter
# server appends to global str and sends back to client
# '' means client is dropping out; when clients are gone,
# server will print final string

# USAGE: python srvr.py port_number

import socket
import sys
import threading

class srvr(threading.Thread):
    # initialize class variables
    v = ''
    vlock = threading.Lock()
    numclntlock = threading.Lock()
    id = 0      # want to give an ID num to each thread starting at 0

    def __init__(self, clntsocket):
        # invoke parent class constructor
        threading.Thread.__init__(self)

        # add instance variables
        self.myid = srvr.id
        srvr.id += 1
        self.myclntsock = clntsocket


    # this func is what thread actually runs;
    # REQUIRED NAME is run();
    # threading.Thread.start() calls threading.Thread.run()
    #       which is always overridden, as we are doing here
    def run(self):
        global num_of_clients

        while True:
            # get letter from client
            k = self.myclntsock.recv(1)

            if k == '':
                srvr.numclntlock.acquire()
                num_of_clients -= 1
                srvr.numclntlock.release()
                break

            # update v in atomic manner
            srvr.vlock.acquire()
            srvr.v += k
            srvr.vlock.release()

            # send v back to client
            self.myclntsock.send(srvr.v)

        self.myclntsock.close()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', int(sys.argv[1])))
s.listen(5)
#s.setblocking(0)

myThreads = []
num_of_clients = 0

conn, addr = s.accept()
clnt_sock = srvr(conn)
myThreads.append(clnt_sock)
clnt_sock.start()
num_of_clients += 1

while num_of_clients > 0:
    conn, addr = s.accept()
    clnt_sock = srvr(conn)

    myThreads.append(clnt_sock)
    clnt_sock.start()
    num_of_clients += 1

s.close()

for s in myThreads:
    s.join()

print "The final value of v is" , srvr.v
