----------------------------- SUMMARY FOR QUICK TESTING ----------------------------------
HwkII.py -- Library for users to use with their code
HwkIIServer.py -- Server code to put on host computers in the system
user.py -- Example code of how a user would code with the library.


1) On HwkII.py, change remote commands to your own username. Note you must have password-
	less login set for CSIF computers for this to work

2) Put HwkIIServer.py in the home directory of the host computers you want as servers. Since CSIF is shared, all pc's will have this file.

3) On interactive mode, import HwkII, and call sysStart() to start system and sysStop() to
	stop system. (User.py connects with port 2500)

4) Servers should now be running. On the terminal, run user.py.

5) In the host computers in the system, you can see in /tmp the files that were created 
	and written to. (a.txt, aa.txt, and aaa.txt -- named this way so it would hash to 
	all three hosts)

6) Stop system by running sysStop() function. Note it might lag for some reason, but is fixed
	by pressing ctrl-C and enter and you can then enter commands quickly again.

------------------------------------------------------------------------------------------


HwkII.py -- Manager:
	
(NOTE YOU MUST CHANGE USER ON SSH COMMAND IN start_servers() and sysStop())

sysStart(['pc5.cs.ucdavis.edu', 'pc8.cs.ucdavis.edu', 'pc28.cs.ucdavis.edu'], 2500)
sysStop(['pc5.cs.ucdavis.edu', 'pc8.cs.ucdavis.edu', 'pc28.cs.ucdavis.edu'])
	
	Manager uses thread module to run servers on each host. We are assuming that all hosts are running on the same port number, so we have a global variable holding the port number so that when we call "sysStop" it terminates the process at a specific port for each host. 
	We noticed that the interactive mode becomes slow after calling sysStart, but pressing "Ctrl-C" and "enter" will make it fast again.




HwkII.py -- Library:

Use these functions as you would with for regular file operations.
If using "import HwkII", you must do "HwkII.dInit()" and "HwkII.dopen()" and for "from HwkII import *", you can omit the "HwkII.".

Functions:
0) dInit(hostList, portnum)
1) dopen(fileName, mode, buffering)
2) dwrite(str)
3) dread(numBytes)	// if you want to read whole file, set numBytes = ''
4) dseek(numBytes)	// not required but included for easier testing
5) dclose()




User.py contains example code of how to use library.


