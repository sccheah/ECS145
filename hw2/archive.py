import os
import thread

def start_servers(hostName, portNum):
    cmd = str('ssh sccheah@' + hostName + ' python /tmp/HwkIIServer.py ' + str(portNum))
    os.system(cmd)

def sysStart(hostList, portNum):
    for host in hostList:
        try:
            thread.start_new_thread(start_servers, (host, portNum))
        except:
            print "Unable to start " + host + " thread."

def sysStop(hostList):
    return
