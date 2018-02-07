# SERVER
# server for remote versions of w and ps commands
# user can check load on machine w/o logging in
# USAGE: python svr.py port_num

import sys, os, socket

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind(('', int(sys.argv[1])))

    while True:
        s.listen(1)

        conn, addr = s.accept()
        command = conn.recv(2)

        pipe = os.popen(command)

        rl = pipe.readlines()
        flo = conn.makefile('w', 0)
        flo.writelines(rl[:-1])

        flo.close()
        conn.close()

if __name__ == '__main__':
    main()
