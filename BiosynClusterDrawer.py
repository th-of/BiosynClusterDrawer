# This draws biosynthetic clusters using the python turtle package

import turtle
# from tkinter import *

# Example input:
# [offset, ["label", start, stop], ["label2", start, stop], ...]
gak = [-50, ["gakA", 4231, 4335], ["gakB", 4422, 4526], ["GakC", 4561, 4659], ["gakI", 4881, 5333]]


turtle.hideturtle()
turtle.speed(5)

# line
turtle.pen(pencolor="black", pensize=4)
turtle.penup()
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(350)
turtle.right(180)
turtle.pendown()
turtle.forward(800)


# arrow
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.pen(fillcolor="red", pencolor="black", pensize=2)
turtle.begin_fill()
turtle.left(30)
turtle.forward(200)
x,y = turtle.xcor(),turtle.ycor()
turtle.left(120)
turtle.forward(200)
turtle.left(120)
turtle.forward(50)
turtle.right(90)
turtle.forward(300)
b = turtle.xcor()
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(50)
turtle.end_fill()
turtle.penup()
turtle.goto((x+b)/2, -100)
turtle.write("gakA", True, align="center", font=("Arial", 40, 'italic'))
ts = turtle.getscreen()
ts.getcanvas().postscript(file="test.eps")
turtle.done()
