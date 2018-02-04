import os
import thread

#class Manager(threading.Thread):
#    def __init__(self, hostList, portNum):
#        threading.Thread.__init__(self)
#        self.hostList = hostList
#        self.portNum = portNum

#    def run(self):
        # this for loop causes an error so that the servers are not run in parallel.
#        for host in self.hostList:
#            start_servers(host, self.portNum)


def start_servers(hostName, portNum):
    cmd = str('ssh sccheah@' + hostName + ' python /tmp/HwkIIServer.py ' + str(portNum))
    os.system(cmd)
    return

#def sysStart(hostList, portNum):
#    system = Manager(hostList, portNum)
#    system.start()

def sysStart(hostList, portNum):
    for host in hostList:
        try:
            thread.start_new_thread(start_servers, (host, portNum))
        except:
            print "Unable to start " + host + " thread."

def sysStop(hostList):
    for host in hostList:
        # forcefully terminate all running processes except
        # login shell, init, and kernel-specific processes
        # wanted to kill just processes from lsof -i with kill $(lsof -i | awk '{print $2}')
        # but it would get open files from local computer rather than host comp
        cmd = str('ssh sccheah@' + host + ' killall5 -9')
        os.system(cmd)

    return
