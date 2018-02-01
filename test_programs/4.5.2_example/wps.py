# client for server for remote versions of w and ps commands

# user can check load on machine w/o logging in

# usage: python wps.py remotehostname port_num {w, ps}
# e.g. "python wps.py nimbus.org 8888 w" would cause server at nimbus.org
#       on port 8888 to run UNIX w command there, and send output of command
#       back to client here

import socket, sys

def main():
    # AF_INET - internet socket; SOCK_STREAM - TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = sys.argv[1]
    port = int(sys.argv[2])
    s.connect((host,port))

    # send w or ps command to server
    s.send(sys.argv[3])

    # create "file-like object" flo
    flo = s.makefile('r', 0) # read-only, unbuffered
    # now can call readlines() on flo, and also use the fact that
    # stdout is a file-like object too
    sys.stdout.writelines(flo.readlines())

if __name__ == '__main__':
    main()
