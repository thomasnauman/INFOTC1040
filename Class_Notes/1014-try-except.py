try:
    file = open("Files/numbers1014.txt", "r")
except FileNotFoundError as e:
    print("File not found")
    print(e)
    # as "e" or any other letter tells you "print the error flavortext"
else:
    file.close()
    print("File is closed")