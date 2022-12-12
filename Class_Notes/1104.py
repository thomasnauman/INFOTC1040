# one-dimensional list
#   Each item in the list is not a list: they can be strings, integers, etc.

# table: NOT a datatype in Python
# can be represented using two-dimensional lists
#   Rows and columns, like in a .csv

# Steps:
# 1. Define a one-dimensional list as usual
table = [] # datatype: table is a list, element datatypes are lists too
# 2. The items are lists
item1 = ["Merchandise", 9.99] # datatype: item1 is a list, element datatypes are strings and floats
item2 = ["Dining", 19.99] # datatype: item2 is a list, element datatypes are strings and floats
# 3. Append the items to the table
table.append(item1)
table.append(item2)
print(table)
# note the double square bracket: [[ implies that there is a list inside the list itself


# indexing
# think of these as nested lists
fruits = ["apple", "banana"]
# first element:
print(fruits[0])
# access the first element in table
print(table[0])
# access the first element in the first element
print(table[0][0])
# access the first element in the second element
print(table[1][0])

# Loop
for item in fruits:
    print(item)

for item in table:
    for element in item:
        print(element)

# Assume all the rows have the same number of elements
# table size is m * n
# m = number of rows, n = number of columns
# the common way of iterating a table is:
    # get the rows
    # then get the columns --OR-STATED-AS--> get the elements in the row
# number of rows = number of elements in table
# number of columns = number of elements in row
for each_row in table:
    for each_column in each_row:
        print(each_column)

# How do we find the number of rows in a table?
print(len(table))
# How do we find the number of rows in a table?
print(len(table[0]))

empty_table = []
if len(empty_table) == 0:
    print("Number of columns is Zero")
else:
    n = len(empty_table[0])
"""    
Given a table of only integers, 
[[1, 2, 3],
[4, 5, 6],
[7, 8, 9]],
calculate sum of all integers
"""
table_of_ints = []
table_of_ints.append([1, 2, 3])
table_of_ints.append([4, 5, 6])
table_of_ints.append([7, 8, 9])
print(table_of_ints)

i = 0
for row in table_of_ints:
    for column in row:
        i += float(column)
print(i)