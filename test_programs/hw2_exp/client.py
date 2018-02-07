import socket
import sys

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
                        # (ASSUMING that is enough for one recv())

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
    data = s.recv(1000000)

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
