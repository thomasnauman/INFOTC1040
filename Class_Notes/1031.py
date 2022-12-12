# how to open and read a file
file_path = "/Users/thomasnauman/PycharmProjects/INFOTC1040/Class Notes/Files/records.txt"
# file object
file = open(file_path)
# Store all the first numbers in each line to a list
ls1 = []
# Store all the second numbers in each line to a list
ls2 = []
# Store all the third numbers in each line to a list
ls3 = []
# a loop
# Modify records.txt: three numbers per line
# Print the three numbers after splitting
# Iteration
for line in file:  # line: a string
    print(line)
    ls = line.split()  # ls: a list
    print(ls)
    n1 = ls[0]
    n2 = ls[1]
    n3 = ls[2]
    print(f"n1 = {n1}")
    print(f"n2 = {n2}")
    print(f"n3 = {n3}")
    ls1.append(float(n1))
    ls2.append(float(n2))
    ls3.append(float(n3))

print(ls1)
# print(ls2)
# print(ls3)
# for loop
# print each item in ls1
# Create a new list ls, ls[i] is 1 + ls1[i]
# ls1 : [2, 3, 5.6, -10]
# ls: [3, 4, 6.6, -9]
ls = []
for n in ls1:
    new_item = n + 1
    # print(new_item)
    ls.append(new_item)
# print(ls)
# Method 2 of for loop
# ls = []
print(f"length of ls1 = {len(ls)}")
# for i in range(4):
# range(4) = 0, 1, 2, 3
for i in range(len(ls1)):
    print(i)
    print(f"The item at index {i} for ls1 = {ls1[i]}")
    print(f"The item at index {i} for ls2 = {ls2[i]}")
    print(f"The item at index {i} for ls3 = {ls3[i]}")
    print(f"The item at index {i} for ls = {ls[i]}")

# print(ls)