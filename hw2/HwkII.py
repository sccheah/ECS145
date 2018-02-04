import os
import thread

def start_servers(hostName, portNum):
    cmd = str('ssh sccheah@' + hostName + ' python /tmp/HwkIIServer.py ' + str(portNum))
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
