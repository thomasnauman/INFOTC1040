# lists
# How to add an element to a list: append, insert
# append adds to the end, insert adds to an index
# lists are mutable (they can be changed)
#   this is in opposition to tuples, which are immutable

# strings
# how to add a character to a string: strings are immutable, so you can only add to the string by concatenating
# and making a new string, saving to the same variable
s1 = "he"
s2 = "llo"
print(s1)
s1 = s1+s2
print(s1)
# s1 is now "hello", used to be "he

# inserting a character to a string
# You have to use string slicing
# turn "he" to "hee"
s1 = "he"
s1 = s1[:2] + "e" + s1[2:]
print(s1)

# turn "This is string" to "This is new string"
s4 = "This is string"
s4 = s4[:8] + "new " + s4[8:]
print(s4)

