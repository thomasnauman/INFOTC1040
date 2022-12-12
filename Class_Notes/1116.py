from turtle import *

def draw_square(t, r, size):
    # repeat forward and left 4 times
    if r == 4:
        pass
    else:
        t.forward(size)
        t.left(90)
        draw_square(t, r+1, size)
"""
draw_maze(bob, 0, 100)
draw_maze(bob, 1, 100-5=95)
draw_maze(bob, 2, 95-5=90)
draw_maze(bob, 3, 90-5=85)
"""

def draw_maze(t, r, size):
    # repeat forward and left 4 times
    if r == 16:
        pass
    else:
        t.forward(size)
        t.left(90)
        draw_maze(t, r+1, size-5)

def draw_circles(t, r, size):
    # repeat forward and left 4 times
    if r == 16:
        pass
    else:
        t.circle(size)
        draw_circles(t, r+1, size-5)
        
def draw_squares(t, r, size):
    # repeat forward and left 4 times
    if r == 16:
        pass
    else:
        # draw the square
        draw_square(t, 0, size)
        t.penup()
        t.forward(5)
        t.left(90)
        t.forward(5)
        t.right(90)
        t.pendown()
        # draw the smaller square -- recursive
        draw_squares(t, r+1, size-10)
def main():
    bob = Turtle()
    bob.speed(1)
    # draw_square(bob, 0, 200)
    # draw_maze(bob, 0, 100)
    # bob.circle(300)
    # draw_circles(bob, 0, 100)
    draw_squares(bob, 0, 300)
    done()
main()