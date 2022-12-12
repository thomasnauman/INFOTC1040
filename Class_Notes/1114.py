# Import everything in turtle
from turtle import *

# Create a turtle
# Turtle: a class
# Nothing in parentheses: initializer looks something like
# def __init__(self):
# A pen is attached to the turtle
# As the turtle moves, the pen will draw
"""
bob = Turtle()
bob.forward(100) # 100 pixels
bob.left(90)
bob.forward(50)
done() # Finish drawing 
"""


def draw_square(t):
    # Move forward four times
    # Turn left three times
    t.forward(100)
    t.left(90)

    t.forward(100)
    t.left(90)

    t.forward(100)
    t.left(90)

    t.forward(100)
    t.left(90)


def draw_square_loop(t):
    for i in range(4):  # 0, 1, 2, 3 -> 4 repitions
        t.forward(100)
        t.left(90)


# We want the function stops after 4 executions
# Add a parameter to keep track of number of executions
# r: number of execution
# 0, 1, 2, 3
def draw_square_recursive(t, r):
    # The case where the recursion:
    # base case
    # Any recursive function MUST have a base case
    # r acts as a way of counting; stop once r = 4 (if you start r = 0, r is number of sides)
    if r == 4:
        pass
    else:
        t.forward(100)
        t.left(90)
        draw_square_recursive(t, r + 1)


# What is recursion?
# Recursion: a function calls itself
# Recursive function
# Easy, convenient, readable -- in SOME cases
# For any recursive function, there's an equivalent
# loop version
def main():
    alice = Turtle()
    alice.speed(2)
    # draw_square(alice)
    # draw_square_loop(alice)
    draw_square_recursive(alice, 0)
    done()


main()