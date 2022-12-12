# sets
#   collection of data
#   bound in curly brackets, separated by commas like a tuple or list
#   distinct entries; you can't have two values called "apple"
myfruits = {"apple", "banana", "cherry"}
print(myfruits)
# properties of sets
#   elements are distinct
myfruits_copy = {"apple", "banana", "cherry", "apple"}
print(myfruits_copy)
# notice how "apple" only prints once

if myfruits == myfruits_copy:
    print("They are the same")
else:
    print("They are different")

#   elements are unordered and unindexed
#       in dictionaries, it is unordered, but Python will print the elements in the order they are entered
#       if you run the program multiple times, the order that it prints elements changes, because their
#       order doesn't matter

# elements are unchangeable
# in a list, you can change the entry at an index; with a set, this is impossible
myfruits_list = ["apple", "banana", "cherry"]
myfruits_list[0] = "pineapple"
print(myfruits_list)

# but you can add and remove elements
myfruits.add("pineapple")
print(myfruits)
myfruits.remove("apple")
print(myfruits)

myfruits = {"apple", "banana", "cherry"}
yourfruits = {"apple", "cherry", "pineapple", "grape"}

mydiff = myfruits.difference(yourfruits)
print(mydiff)
# this prints what "myfruits" has that "yourfruits" doesn't

yourdiff = yourfruits.difference(myfruits)
print(yourdiff)
# this prints what "yourfruits" has that "myfruits" does not

intersect = myfruits.intersection(yourfruits)
print(intersect)
# this prints what "myfruits" and "yourfruits" have in common

onion = myfruits.union(yourfruits)
print(onion)
# this prints the combination of "myfruits" and "yourfruits"

disjoint = myfruits.isdisjoint(yourfruits)
print(disjoint)
# returns True or False; disjoint is if there is no intersection
#   False means that there is some joint, or some intersection

myfruits_list = ["apple", "banana", "cherry"]
myfruits_list.pop()
print(myfruits_list)
# gets rid of the last item in a list

print(myfruits)
myfruits.pop()
print(myfruits)
# this gets rid of a random element; since there is no defined index myfruits[-1], it just deletes a random one
# you should use the remove function if you want to get rid of something