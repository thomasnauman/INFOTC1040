print("Hello World")

print(3+5)

# What is a variable?
# What is a function?
# Imports: Predefined functions that are contained in libraries; we will have to import them from those libraries

# Variables: variables are used to sub-in for a function or for a series of operations, a string, etc.
print((3+5) * 4)

x = 3+5
y = x*4

# Data Types
# Integer: 3, 5, 1, 2, etc.
# String: "Hello", "World", "Datatype", etc.
# Floating Point: 1.2, 3.2, 4.693, etc.

s = "Hello World"
print(s)

f = 2.3
print(f)

print(3.1 + 5.8)
# the "+" is an operator: it operates on something
print("Hello" + " " + "World")
# concatenation: putting two strings together

# Functions: takes some inputs and produces an output; returns an output
# print is a function

def put_them_together(a, b):
    return (a + b)

def advanced_put_them_together(a, b):
    print(str("{} {}".format(a, b)))

print(put_them_together("Hello ", "World"))
advanced_put_them_together("Hello", "World")
advanced_put_them_together("Hello", 1)

hw = advanced_put_them_together("Hello ", "World")
hw