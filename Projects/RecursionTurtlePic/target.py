from turtle import *

pen = Turtle()


def board(t, c, d):
    t.goto(-d, -d)
    t.color(f'{c}')
    t.begin_fill()
    for i in range(4):
        t.forward(2 * d)
        t.left(90)
    t.end_fill()


def come_back(t):
    t.penup()
    t.home()
    t.pendown()


def concentric(t, r, s):
    if r >= 10:
        pass
    else:
        if r % 2 == 0:
            t.color("white")
        else:
            t.color("red")
        come_back(t)
        t.begin_fill()
        t.penup()
        t.left(270)
        t.forward(s)
        t.left(90)
        t.pendown()
        t.circle(s)
        t.end_fill()
        come_back(t)
        concentric(t, r + 1, s - 40)


def main():
    pen.speed(100)
    board(pen, 'green', 400)
    board(pen, 'tan', 370)
    concentric(pen, 0, 350)
    done()


main()
