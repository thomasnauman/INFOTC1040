# math operator: +
# operand: the things you put next to the +; depending on the data type, the operand has different uses
    # 1 + 2 will perform a math operation
    # "One" + "Two" will concatenate them, since they are strings

# math operator: -
print(1-2)
# print("Hello" - "H") will not work, as you cannot subtract strings from each other

# math operator: "*" for multiplication
# math operators: "/" and "//" for division
    # / will give a float value
    # // will give a fixed point value
print(5/2)
print(5.0/2)
print(5//2)
print(5.0/2.0)
print(6.0/3.0)

# special usage of the multiplication sign: * with strings
print("Hello " * 3)
    # this printed "Hello " 3 times; it is a "Pythonic" operation

def foo(a):
    return a + 1

print(foo(5))

six = foo(5)
print(six)


