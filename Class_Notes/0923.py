# lists
fruits = ["apple", "banana", "cherry"]
print(fruits)
fruits.append("orange")
print(fruits)
#   append functions will add an item to the last index of the list (list[-1])
print(fruits[-1])

fruits.insert(1, "mango")
print(fruits)
# insert requires two arguments: the index you insert into, and what you are inserting
#   this function added "mango" to index 1

i = 0
for fruit in fruits:
    print("The fruit in index",[i],"is",fruit)
    i += 1

del fruits[1]
print(fruits)
# this deletes the item at whatever index you select

fruits.pop()
print(fruits)
# pop removes the last index of the list (list[-1])

# method 1
def modify_list(ls):
    for x in ls:
        x = x + "_myfruit"

def modify_number(n):
    new = n + 5
    return new

modify_list(fruits)
print(fruits)


# length of a list: size of the list, number of elements in the list
print(len(fruits))

# range: start, stop, step
# start is the number you start counting from, stop is where you end (but don't include), step is "what you count by"
# (1's, 2's, etc.)
# start and step are optional; they default to 0 and 1 respectively if you don't include them (starts at 0, counts by 1)

# method 2
for i in range(3):
    print(fruits[i])
# out of range error
    # if you have fewer list items than indices you specify, then there is an out of range error
for i in range(len(fruits)):
    print(fruits[i])
    # this solves the out of range error; it only counts as far as the length of the list extends

x = 3
modify_number(x)
print(x)
print(modify_number(x))
# integers are immutable
# lists are mutable
# tuples are like lists, but they are immutable

