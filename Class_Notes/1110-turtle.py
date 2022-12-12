import turtle
import math

bob = turtle.Turtle()

# bob.forward(100)
# bob.left(45)
# bob.forward(100)
# bob.right(90)
# bob.forward(100)

# square
# bob.color("red", "cyan")
#
# bob.begin_fill()
# bob.forward(100)
# bob.left(90)
# bob.forward(100)
# bob.left(90)
# bob.forward(100)
# bob.left(90)
# bob.forward(100)
# bob.left(90)
#
# bob.penup()
# bob.forward(100)
# bob.pendown()
#
# bob.begin_fill()
# bob.forward(100)
# bob.left(90)
# bob.forward(100)
# bob.left(90)
# bob.forward(100)
# bob.left(90)
# bob.forward(100)
# bob.left(90)
# bob.end_fill()

# flower

# bob.color("red", "yellow")
# bob.speed(10000000)
#
# for i in range(2000):
#     bob.forward(math.sqrt(i))
#     bob.left(i%180)

# recursive

def star(turtle, size):
    if size <= 10:
        return
    else:
        for i in range(5):
            turtle.forward(size)
            star(turtle, size/2)
            turtle.left(216)

star(bob, 100)
turtle.done()