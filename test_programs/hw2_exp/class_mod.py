class myClass:
    #host = str()
    hostList = []
    portNum = int()

    def __init__(self, fileName):
        self.fileName = fileName

    def dread(self):
        print "successfully read"
        print self.fileName
        print myClass.hostList
        print myClass.portNum


def dInit(host_list, portNum):
    myClass.hostList = host_list
    myClass.port = portNum


def dopen(fileName):
    return myClass(fileName)
