import socket
import sys
import threading

class srvr(threading.Thread):
    def __init__(self, conn):
        # invoke parent class constructor
        threading.Thread.__init__(self)
        self.conn = conn
        self.instructions = ""


    def run(self):

        numMsgBytes = self.conn.recv(1024)
        #print numMsgBytes
        self.conn.send(' ')
        # get instructions from client
        self.instructions = self.conn.recv(int(numMsgBytes))         # accepts up to numMsgBytes of data
        self.instructions = self.instructions.split()         # split instructions up into a list
        #print self.instructions

        # route the requested operation
        if self.instructions[0] == "dopen":
            dopen(self.conn, self.instructions[1:])
        if self.instructions[0] == "dclose":
            dclose(self.conn, self.instructions[1:])
        if self.instructions[0] == "dread":
            dread(self.conn, self.instructions[1:])
        if self.instructions[0] == "dwrite":
            dwrite(self.conn, self.instructions[1:])
        if self.instructions[0] == "dseek":
            dseek(self.conn, self.instructions[1:])

        # close connected socket
        self.conn.close()

# create global dictionary to manipulate file
file_descriptors = {}

# func to call standard func open()
def dopen(conn, instructions):
    global file_descriptors

    # check if length of instructions is enough to satisfy command
    if len(instructions) == 3:
        fileName = instructions[0]
        accessMode = instructions[1]
        buffering = instructions[2]

        # open file and store file descriptor into variable
        fp = open(fileName, accessMode, int(buffering))
        file_descriptors[fileName] = fp      # store int dictionary(key: fileName, value: filedescriptor)

    if fp:
        conn.send("Opened " + fileName + " successfully!")
    else:
        conn.send("Failed to open " + fileName)
    return

# func to call standard func read()
def dread(conn, instructions):
    global file_descriptors

    if len(instructions) > 0:
        fileName = instructions[0]

    # check to see if we have a byte number specified, if yes, run read(n), else read()
    if len(instructions) == 2:
        numBytes = instructions[1]
        data = file_descriptors[fileName].read(int(numBytes))
    else:
        data = file_descriptors[fileName].read()

    conn.send(str(sys.getsizeof(data)))
    conn.recv(1)
    conn.sendall(data)

    return

# func to call standard func seek()
def dseek(conn, instructions):
    global file_descriptors

    if len(instructions) == 2:
        fileName = instructions[0]
        numBytes = instructions[1]

    try:
        file_descriptors[fileName].seek(int(numBytes))
        #print "Seeking byte \'" + numBytes + "\' in " + fileName + " successful."
    except:
        pass
        #print "Seeking byte \'" + numBytes + "\' in " + fileName + " failed."

    return

# func to call standard func write()
def dwrite(conn, instructions):
    global file_descriptors

    # make sure we have enough arguments
    if len(instructions) >= 2:
        fileName = instructions[0]
        my_str = " ".join(instructions[1:])         # want to join rest of list into a string

    try:
        file_descriptors[fileName].write(my_str)
        conn.send("Successfully written to " + fileName + "!")
    except:
        conn.send("Failed writing to " + fileName + "!")

    return

# func to call standard func close()
def dclose(conn, instructions):
    global file_descriptors

    if len(instructions) >= 1:
        fileName = instructions[0]
        file_descriptors[fileName].close()
        del file_descriptors[fileName]

        # make sure that the filename specified is in file_descriptors keys
        if fileName not in file_descriptors:
            conn.send("Closed " + fileName + " successfully!")
        else:
            conn.send("Failed to close " + fileName)

    return

# create listening socket, bind it, and allow up to 5 pending connections
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', int(sys.argv[1])))
s.listen(5)

# keep looping for new connection requests and executing necessary operations
while True:
    conn, addr = s.accept()
    clnt_sock = srvr(conn)
    clnt_sock.start()

# close listening socket
s.close()
