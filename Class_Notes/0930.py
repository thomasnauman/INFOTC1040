# strings
# characters
    # only one letter or place in a string; "c", "8"
print("\u00A9")
# these are unicode symbols
# in other languages, characters are a special datatype, just like integers
#   in other languages, strings are arrays of characters
# in python, characters are not a special datatype; characters are just strings with a length of 1

# arrays vs. python lists
# python doesn't have arrays
#   array: they occupy some contiguous memory blocks
#   Python lists: they occupy memory blocks all over the place

# Python: strings are a bunch of characters
ap = "apple"
ap2 = 'apple'
sentence = "John says, 'This week's challenge is easy'."
# you have to use single quotations if you have a quotation within a string; otherwise, python will read it wrong
print(sentence)

# multiline strings
# bound by 3 quotations (""") on each side
long = """This
is
a
multiline
string"""
print(long)

# format method
name = "John"
age = 81

name_and_age = name + " is " + str(age) + " years old"
print(name_and_age)

format_name_and_age = "{} is {} years old".format(name, age)
print(format_name_and_age)

alt_format_name_and_age = "{name} is {age} years old".format(age = age, name = name)
print(alt_format_name_and_age)

# f strings
f_format_name_and_age = f"{name} is {age:.2f} years old"
print(f_format_name_and_age)

# :f will print it as a floating point number
# the .x will print it with x amount of places (2 in this case)

