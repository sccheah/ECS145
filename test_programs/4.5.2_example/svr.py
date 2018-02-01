# SERVER
# server for remote versions of w and ps commands
# user can check load on machine w/o logging in
# USAGE: python svr.py port_num

import socket, sys, os

def main():
    ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = int(sys.argv[1])
    ls.bind(('', port))

    while (1):
        ls.listen(1)
        conn, addr = ls.accept()

        print "client is at", addr

        rc = conn.recv(2)
        ppn = os.popen(rc)
        rl = ppn.readlines()

        flo = conn.makefile('w', 0)
        flo.writelines(rl[:-1])

        flo.close()
        conn.close()

if __name__ == "__main__":
    main()
