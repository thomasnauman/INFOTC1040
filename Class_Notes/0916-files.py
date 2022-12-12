# open() will open the file, creates a file object that points to the actual file
# the default mode is read mode
# you have to open it in write mode if you want to write to it - writes over it
# to be able to read and write, you need to open them in the r+ or w+ modes
# to append: open in append mode -- "a"
f = open("/Class Notes/Files/test_file", "r+")
#print(f.read())
#f.write("\nLet's modify the file")
#f.close

# at the end of each line, there is a newline character: \n

# read the file line by line
for line in f:
    print(line)