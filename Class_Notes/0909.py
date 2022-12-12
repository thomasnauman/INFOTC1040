# conditionals
# boolean data type in lists and conditionals

print(1 == 2)
# this yields false, since 1 =/= 2

print(1 != 2)
# this yields true, since 1 =/= 2

# conditional: if something is true,:
# then do something
# syntax: if ____ is _____:
            # _______
        # else:
            # ------

a = 33
b = 200
if b > a:
    print("b is greater than a")
    print("b =", b, "a =", a)
elif b == a:
    print("b is equal to a")
    print("b =", b, "a =", a)
else:
    print("b is less than a")
    print("b =", b, "a =", a)


# algorithm: list of steps that need to be done to solve a problem
def main():
    # let user input number
    num = int(input("Input a number: "))
    # divide by two and check the remainder
    remainder = num % 2
    # if remainder is 1, number is odd and print it is odd
    if remainder == 1:
        print(num, "is odd")
    # if remainder is 0, number is even and print it is even
    else:
        print(num, "is even")


main()

# datatypes: integers, floats, strings, booleans
# tuple: (1, 2, "Three", 4.5)
# list: [1, 2, "Three", 4.5] - ordered collection of data
    # e.x. nums = [1, 2, 1, 3, 1, 5]
    # e.x. foods = ["Banana", "Strawberry", "Apple"]
import math
def calculate_perimeter(radius):
    perimeter = 2 * math.pi * radius
    return perimeter

def radius():
    list_of_radius = [2, 2.1, 23.4, 7.7]
    for number in list_of_radius:
        if number < 0:
            print("Enter a positive number.")
        else:
            perimeter = (calculate_perimeter(number))
            print(perimeter)

# radius()