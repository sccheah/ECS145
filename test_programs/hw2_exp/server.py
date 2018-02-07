import socket
import sys


# create global dictionary to manipulate file
file_pointers = {}


def dopen(conn, instructions):
    global file_pointers

    fileName = instructions[0]
    accessMode = instructions[1]
    buffering = instructions[2]
    fp = open(fileName, accessMode, int(buffering))

    if fp:
        conn.send("Opened " + fileName + " successfully!")
    else:
        conn.send("Failed to open " + fileName)

    file_pointers[fileName] = fp

    return

def dread(conn, instructions):
    global file_pointers

    fileName = instructions[0]
    if len(instructions) == 2:
        numBytes = instructions[1]
        data = file_pointers[fileName].read(int(numBytes))
    else:
        data = file_pointers[fileName].read()

    conn.send(data)

    return

def dseek(conn, instructions):
    global file_pointers

    fileName = instructions[0]
    numBytes = instructions[1]

    try:
        file_pointers[fileName].seek(int(numBytes))
        print "Seeking byte \'" + numBytes + "\' in " + fileName + " successful."
    except:
        print "Seeking byte \'" + numBytes + "\' in " + fileName + " failed."

    return

def dwrite(conn, instructions):
    global file_pointers

    fileName = instructions[0]
    my_str = " ".join(instructions[1:])

    try:
        file_pointers[fileName].write(my_str)
        conn.send("Successfully written to " + fileName + "!")
    except:
        conn.send("Failed writing to " + fileName + "!")

    return



def dclose(conn, instructions):
    global file_pointers

    fileName = instructions[0]
    file_pointers[fileName].close()
    del file_pointers[fileName]

    if fileName not in file_pointers:
        conn.send("Closed " + fileName + " successfully!")
    else:
        conn.send("Failed to close " + fileName)

    return

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', int(sys.argv[1])))

s.listen(5)
#print "here"
while True:
    conn, addr = s.accept()

    instructions = conn.recv(1024)
    instructions = instructions.split()
    print instructions

    if instructions[0] == "dopen":
        dopen(conn, instructions[1:])
    if instructions[0] == "dclose":
        dclose(conn, instructions[1:])
    if instructions[0] == "dread":
        dread(conn, instructions[1:])
    if instructions[0] == "dwrite":
        dwrite(conn, instructions[1:])
    if instructions[0] == "dseek":
        dseek(conn, instructions[1:])

    conn.close()
