import os
import socket

# TODO: test remotely in csif (check if hashing works); go through code and make it more efficient
# TODO: comment code, recheck to see if going according to hw specs, README 

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

def dopen(fileName, accessMode, buffering):
    global hostList
    global portNum
    buffering = str(buffering)      # cannot send int through socket, so cast to str

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = hostList[hash(fileName) % len(hostList)]
    s.connect((host, portNum))

    delim = " "
    seq = ("dopen", fileName, accessMode, buffering)
    instructions = delim.join(seq)
    #print instructions

    s.send(instructions)

    confirm = s.recv(1024)   # receive up to 1024 bytes


    print confirm
    s.close()

    return

def dread(fileName, numBytes):
    global hostList
    global portNum
    numBytes = str(numBytes)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = hostList[hash(fileName) % len(hostList)]
    s.connect((host, portNum))

    delim = " "
    seq = ("dread", fileName, numBytes)
    instructions = delim.join(seq)
    s.send(instructions)

    data = s.recv(1024)
    while True:
        tmp = s.recv(1024)

        if not tmp:
            break

        data += tmp

    if data:
        print "Successfully received data from " + fileName + "!"
    else:
        print "Data retrieval unsuccessful from " + fileName + "!"

    s.close()
    return data


def dseek(fileName, numBytes):      # not required; writing for debugging
    global hostList
    global portNum
    numBytes = str(numBytes)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = hostList[hash(fileName) % len(hostList)]
    s.connect((host, portNum))

    delim = " "
    seq = ("dseek", fileName, numBytes)
    instructions = delim.join(seq)
    s.send(instructions)

    s.close()

    return


def dwrite(fileName, my_str):
    global hostList
    global portNum
    my_str = str(my_str)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = hostList[hash(fileName) % len(hostList)]
    s.connect((host, portNum))

    delim = " "
    seq = ("dwrite", fileName, my_str)
    instructions = delim.join(seq)

    s.send(instructions)
    confirm = s.recv(1024)

    print confirm
    s.close()

    return


def dclose(fileName):
    global hostList
    global portNum

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = hostList[hash(fileName) % len(hostList)]
    s.connect((host, portNum))

    delim = " "
    seq = ("dclose", fileName)
    instructions = delim.join(seq)

    s.send(instructions)
    confirm = s.recv(1024)

    print confirm
    s.close()

    return
