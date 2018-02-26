# Example how a user would use the library.

# if using "import HwkII", only difference from this code is
#       that you would prepend dInit() and dopen() with module name.
#       The other functions don't need to because they are methods of class from module
from HwkII import *

dInit(['pc5.cs.ucdavis.edu', 'pc9.cs.ucdavis.edu', 'pc28.cs.ucdavis.edu'], 2500)
#dInit(['localhost'], 2501)

# open file (create if does not exist). Named a.txt, aa.txt, and aaa.txt to
#       test hashing function is working properly
fp1 = dopen("/tmp/a.txt", 'a+', 0)
fp2 = dopen("/tmp/aa.txt", 'a+', 0)
fp3 = dopen("/tmp/aaa.txt", 'a+', 0)

# write a string five times to each file
fp1.dwrite("hello file a.txt" * 5)
fp2.dwrite("hello file aa.txt" * 5)
fp3.dwrite("hello file aaa.txt" * 5)

# move the file position
fp1.dseek(0)
fp2.dseek(0)
fp3.dseek(0)

# read all files to it's entirety
data = fp1.dread('')
print "fp1 data: ", data, '\n\n'
data = fp2.dread('')
print "fp2 data: ", data, '\n\n'
data = fp3.dread('')
print "fp3 data: ", data, '\n\n'

# move file position again
fp1.dseek(0)
fp2.dseek(0)
fp3.dseek(0)

# test append function of write
fp1.dwrite("APPENDING STRING1")
fp2.dwrite("APPENDING STRING2")
fp3.dwrite("APPENDING STRING3")

# move file position
fp1.dseek(0)
fp2.dseek(0)
fp3.dseek(0)

# read files to it's entirety again
data = fp1.dread('')
print "fp1 data: ", data
data = fp2.dread('')
print "fp2 data: ", data
data = fp3.dread('')
print "fp3 data: ", data

# close all files
fp1.dclose()
fp2.dclose()
fp3.dclose()
