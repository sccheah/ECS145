import os
import sys
import socket
import thread

################################## MANAGER CODE ########################################

# thread to start server on each host
def start_servers(hostName, portNum):
    # create command to issue remote command to start server
    cmd = str('ssh sccheah@' + hostName + ' python HwkIIServer.py ' + str(portNum))
    os.system(cmd)          # execute command
    return

# manager calls this function to start the system (servers on all hosts)
def sysStart(hostList, portNum):
    global sys_port         # keep port number for shutting off system
    sys_port = portNum

    # iterate through list of hosts and start a thread to run server
    for host in hostList:
        try:
            thread.start_new_thread(start_servers, (host, portNum))
        except:
            pass
            #print "Unable to start " + host + " thread."

# manager calls this to stop the system (stop servers on all hosts)
def sysStop(hostList):

    # iterage through list of hosts and stop
    for host in hostList:
        # kills process at specific port #
        cmd = str('ssh sccheah@' + host + ' fuser -k ' + str(sys_port) + '/tcp')
        os.system(cmd)

    return

#################################### CLIENT CODE #########################################

# class that acts as a file descriptor
class FileDescriptor:
    hostList = []       # class variable to hold list of hosts
    portNum = int()     # class var to hold port number
                        #       ASSUMING SERVERS ON ALL HOSTS ARE ON SAME PORT NUM

    # constructor that initializes property to hold filenames
    def __init__(self, fileName):
        self.fileName = fileName

    # method that reads n bytes from file (to read whole file, set param numBytes: '')
    def dread(self, numBytes):
        global hostList
        global portNum
        numBytes = str(numBytes)        # type cast to str in case int was entered
        data = str()

        # create socket, connect to specific host by hashing filename
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = hostList[hash(self.fileName) % len(hostList)]
        s.connect((host, portNum))

        # separate all necessary data to perform op with spaces and send it
        delim = " "
        seq = ("dread", self.fileName, numBytes)
        instructions = delim.join(seq)

        # separate the os buffer to send the correct message
        s.send(str(sys.getsizeof(instructions)))
        s.recv(1)
        s.send(instructions)

        # get the size of the message and read the entire message
        numMsgBytes = s.recv(1024)
        #print numMsgBytes
        s.send(' ')
        data = s.recv(int(numMsgBytes))

        # if data:
        #     print "Successfully received data from " + self.fileName + "!"
        # else:
        #     print "Data retrieval unsuccessful from " + self.fileName + "!"sys.getsizeof(myint)

        s.close()
        return data

    # seek function to move fp to numBytes into the file
    def dseek(self, numBytes):      # not required; writing for easier debugging
        global hostList
        global portNum
        numBytes = str(numBytes)

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = hostList[hash(self.fileName) % len(hostList)]
        s.connect((host, portNum))

        delim = " "
        seq = ("dseek", self.fileName, numBytes)
        instructions = delim.join(seq)

        # separate the os buffer to send the correct message
        s.send(str(sys.getsizeof(instructions)))
        s.recv(1)
        s.send(instructions)

        s.close()
        return

    # func to write str into file
    def dwrite(self, my_str):
        global hostList
        global portNum
        my_str = str(my_str)

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = hostList[hash(self.fileName) % len(hostList)]
        s.connect((host, portNum))

        delim = " "
        seq = ("dwrite", self.fileName, my_str)
        instructions = delim.join(seq)

        # separate the os buffer to send the correct message
        s.send(str(sys.getsizeof(instructions)))
        s.recv(1)
        s.sendall(instructions)

        confirm = s.recv(1024)
        # print confirm

        s.close()
        return

    # func to close file
    def dclose(self):
        global hostList
        global portNum

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = hostList[hash(self.fileName) % len(hostList)]
        s.connect((host, portNum))

        delim = " "
        seq = ("dclose", self.fileName)
        instructions = delim.join(seq)

        # separate the os buffer to send the correct message
        s.send(str(sys.getsizeof(instructions)))
        s.recv(1)
        s.send(instructions)

        confirm = s.recv(1024)
        # print confirm

        s.close()
        return

# create global var storing hostlist and portNum
def dInit(host_list, port_num):
    global hostList
    global portNum

    hostList = host_list
    portNum = port_num

# func to open file. returns an instance of FileDescriptor
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

    # separate the os buffer to send the correct message
    s.send(str(sys.getsizeof(instructions)))
    s.recv(1)
    s.send(instructions)

    confirm = s.recv(1024)   # receive up to 1024 bytes
    # print confirm

    s.close()
    return FileDescriptor(fileName)
