# client for server for remote versions of w and ps commands

# user can check load on machine w/o logging in

# usage: python wps.py remotehostname port_num {w, ps}
# e.g. "python wps.py nimbus.org 8888 w" would cause server at nimbus.org
#       on port 8888 to run UNIX w command there, and send output of command
#       back to client here


import socket, sys

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = sys.argv[1]
    port = int(sys.argv[2])

    s.connect((host, port))
    s.send(sys.argv[3])

    flo = s.makefile('r', 0)
    sys.stdout.writelines(flo.readlines())

    s.close()

if __name__ == '__main__':
    main()
