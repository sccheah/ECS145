import HwkII

HwkII.dInit(["localhost"], 2500)

HwkII.dopen("test_write.txt", "w+", 0)
HwkII.dwrite("test_write.txt", "hello there")
HwkII.dclose("test_write.txt")

HwkII.dopen("example_file.txt", 'r+', 0)
data = HwkII.dread("example_file.txt", '')        # second arg is the size of bytes
print "Before write: ", data


HwkII.dclose("example_file.txt")
HwkII.dopen("example_file.txt", 'a+', 0)


HwkII.dseek("example_file.txt", 0)

my_str = "This string should append to the file"
HwkII.dwrite("example_file.txt", my_str)
HwkII.dseek("example_file.txt", 0)
data = HwkII.dread("example_file.txt", '')
print "After writing to file: ", data


HwkII.dclose("example_file.txt")

#print fp

#f = file(fp)
#print f
