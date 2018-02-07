import os
import threading
import thread

def start_servers(hostName, portNum):
    cmd = str('ssh sccheah@' + hostName + ' python /HwkIIServer.py ' + str(portNum))
    os.system(cmd)
    return

def sysStart(hostList, portNum):
    global port
    port = portNum

    for host in hostList:
        try:
            thread.start_new_thread(start_servers, (host, portNum))
        except:
            print "Unable to start " + host + " thread."

def sysStop(hostList):
    for host in hostList:
        # --wanted to kill just processes from lsof -i with kill $(lsof -i | awk '{print $2}')
        #cmd = str('ssh sccheah@' + host + ' killall5 -9')
        # kills process at specific port #
        cmd = str('ssh sccheah@' + host + ' fuser -k ' + str(port) + '/tcp')
        os.system(cmd)

    return

# create global var storing hostlist and portNum
def dInit(host_list, port_num):
    global hostList
    global portNum

    hostList = host_list
    portNum = port_num

# read from file
def dread(fp, bytes):
    global hostList
    global portNum

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((hostList, portNum))
    s.send("dread")
    s.send(fp)
    s.send(bytes)

    data = s.recv(bytes)
    s.close()
    return data

# write to file
def dwrite(fp, fileName):
    global hostList
    global portNum

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((hostList, portNum))
    s.send("dwrite")
    s.send(fp)
    s.send(fileName)

    # dont need to recv() anything
    s.close()           # close socket

    return

# open file
def dopen(fileName, accessMode, buffering):
    global hostList
    global portNum

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # add code to do multiple hosts/clients.
    # for now assume singular connection

    s.connect((hostList, portNum))      # connect with server
    s.send("dopen")                     # tell server what func to run
    s.send(fileName)                    # send filename to server
    s.send(accessMode)                  # send accessMode to server
    s.send(buffering)                   # send buffering code to server

    fp = s.recv(1024)   # receive up to 1024 bytes
                        # (ASSUMING that is enough for one recv())
    s.close()
    return fp

# TODO: close file
def dclose(fp):
    global hostList
    global portNum

    # maybe use reference to object to know which file to close
    # or just automatically close files in server each time...

    # try to send fp reference? relevant if we keep fp in server-side open
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostList, portNum))

    s.send("dclose")            # tell server what func to run
    s.send(fp)                # send which file to close

    # dont have to recv(?)
    s.close()

    return
