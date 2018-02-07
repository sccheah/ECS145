import client

client.dInit("localhost", 2500)

client.dopen("example_file.txt", 'r+', 0)
data = client.dread("example_file.txt", '')        # second arg is the size of bytes
print "Before write: ", data


client.dclose("example_file.txt")
client.dopen("example_file.txt", 'a+', 0)


client.dseek("example_file.txt", 0)

my_str = "This string should append to the file"
client.dwrite("example_file.txt", my_str)
client.dseek("example_file.txt", 0)
data = client.dread("example_file.txt", '')
print "After writing to file: ", data


client.dclose("example_file.txt")

#print fp

#f = file(fp)
#print f
