# write a program that reads the numbers in the "numbers.txt" file
input_file = open("/Users/thomasnauman/PycharmProjects/INFOTC1040/Class Notes/Files/numbers", "r+")
    # the open function should point to where the file is on the computer's file system
    # this is like double-clicking the file; it doesn't do anything besides just loads the file into memory

# print(input_file.read())

    # this reads the file all at once
"""
print(input_file.readline())
print(input_file.readline())
print(input_file.readline())
print(input_file.readline())
print(input_file.readline())
"""
    # each instance of readline() prints one line, the next prints the next, etc.

#for line in input_file:
    #print(line)
    # this reads the file line by line: for each line in "input_file", read the line

# write a program that reads the numbers in the file and for each number, time 10 and saves the results
# to a new file called "results.txt"
    # turn it into a float
    # takes one line
ten_times = open("/Users/thomasnauman/PycharmProjects/INFOTC1040/Class Notes/Files/results", "r+")
for line in input_file:
    result = (float(line)*10)
    ten_times.write(str(result) + "\n")
ten_times.close

ten_times = open("/Users/thomasnauman/PycharmProjects/INFOTC1040/Class Notes/Files/results", "r+")
print(ten_times.read())
ten_times.close

