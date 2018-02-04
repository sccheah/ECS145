Manager:
sysStart(['pc5.cs.ucdavis.edu', 'pc8.cs.ucdavis.edu', 'pc28.cs.ucdavis.edu'], 2500)
sysStop(['pc5.cs.ucdavis.edu', 'pc8.cs.ucdavis.edu', 'pc28.cs.ucdavis.edu'])
	
	Manager uses thread module to run servers on each host. We are assuming that all hosts are running on the same port number, so we have a global variable holding the port number so that when we call "sysStop" it terminates the process at a specific port for each host. 
	We noticed that the interactive mode becomes slow after calling sysStart, but pressing "Ctrl-C" and "enter" will make it fast again.

