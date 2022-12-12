# create a dictionary
# dict = {key1:value1, key2:value2, key3:value3}

# create a dictionary for classes in IT
# keys are class numbers (integer), values are class names (strings)
    # keys have to be an immutable datatype
    # values can be any datatype
classes_dict = {1040: "Introduction to Problem Solving and Programming",
                1000: "Intro to IT",
                1600: "Digital Systems"}

# common methods of using dictionaries

# access an element in dictionary
# 1) Using [] similar to a list index
print(classes_dict[1040])
    #print(classes_dict[1044])
    # returns an error because key "1044" doesn't exist in the dictionary
# 2) Using get()
print(classes_dict.get(1040))
print(classes_dict.get(1044))
    # means that the key does not exist
# check if a key exists
if classes_dict.get(1044) == None:
    print("Key 1044 DNE")

# updating a dictionary

# change the value of a key in the dictionary
# 1) Using []
print(classes_dict[1000])
classes_dict[1000] = "Introduction to IT"
print(classes_dict[1000])

# 2) Using update() function
print(classes_dict[1040])
classes_dict.update({1040:"Introduction to Python"})
print(classes_dict[1040])

# adding an element to dictionary
classes_dict[1044] = "Fake Class"
print(classes_dict[1044])
classes_dict[1001] = "Fake Class #2"
print(classes_dict[1001])

print(classes_dict)

# deleting an element from dictionary
del classes_dict[1001]
print(classes_dict)

# how to loop through a dictionary

# this prints keys, not values
for key in classes_dict:
    print(key)

# this prints values, not keys
for key in classes_dict:
    print(classes_dict[key])

# this prints keys and values
for key in classes_dict:
    print(f"Class {key}'s title is {classes_dict[key]}")

# this prints keys and values
for key, value in classes_dict.items():
    print(key, value)

print(classes_dict.items())
# this returns tuples of each key:value pair

print(classes_dict.keys())
# this returns all the keys

print(classes_dict.values())
# this returns all values
