# reading csv

# review how to read a space separated file
file = open("Files/numbers1017.txt", "r+")
for line in file:
    items = line.split()
    print(items)
file.close()

filecsv = open("Files/numbers1017.csv", "r+")
for line in filecsv:
    items = line.split(",")
    print(items)
filecsv.close()