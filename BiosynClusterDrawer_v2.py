# This draws biosynthetic clusters using the python turtle package

# import turtle
from turtle import *
import turtle
import math
import numpy as np
# from tkinter import *

# Example input:
# [offset, ["label", start, stop], ["label2", start, stop], ..., offset]
# Promoters and terminators are identified as lists of length 2:
# PR = promoter reverse, PF = promoter forward. T = terminator
gak = [-50, ["gakA", 4231, 4335, "blue", "P"], ["gakB", 4422, 4526, "blue", "P"], ["gakC", 4561, 4659, "blue", "P", "T"],  ["gakI", 5333, 4881, "red", "T"], ["cro", 5517, 5290, "black", "P", "T"]]

orfs = []

for i in gak:
    if type(i) is list and len(i) > 2:
        orfs.append(i)

vals = []
for i in gak:
    if type(i) is int:
        vals.append(i)
    else:
        for a in i:
            if type(a) is int:
                vals.append(a)

valsarray = np.asarray(vals)
valsarray[0] = valsarray[1]+valsarray[0]
valsarray = valsarray-valsarray[0]
clusterlength = max(valsarray)+50

offset = -50

#Circle radius for terminator symbol
tcircrad = 15

# hide turtle and set draw speed

turtle.setup(width=3000, height=1080, startx=0, starty=0)
turtle.screensize(3000, 1080)
turtle.hideturtle()
turtle.speed(10)

# line
turtle.penup()
turtle.right(180)
turtle.forward(clusterlength*0.5)
turtle.right(180)
turtle.pendown()
turtle.pen(pencolor="black", pensize=4)
turtle.forward(clusterlength)


## draw orfs

turtle.penup()
turtle.right(180)
turtle.forward(clusterlength+offset)
a,b = turtle.xcor(),turtle.ycor()
print(a,b)
turtle.right(90)
turtle.pendown()
a = 0
for n in orfs:
    turtle.pen(fillcolor=n[3], pencolor="black", pensize=4)
    turtle.begin_fill()
    if n[1] < n[2]:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.right(90)
        turtle.forward((float(n[2]) - float(n[1]) - math.tan(math.radians(30)) * 100))
        turtle.left(90)
        turtle.forward(50)
        turtle.right(150)
        turtle.forward(115.47)
        x,y = turtle.xcor(),turtle.ycor()
        turtle.right(60)
        turtle.forward(115.47)
        turtle.right(150)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward((float(n[2]) - float(n[1]) - math.tan(math.radians(30)) * 100))
        turtle.right(90)
        turtle.forward(50)
        k,l = turtle.xcor(),turtle.ycor()
        turtle.end_fill()
        if 'T' in n:
            turtle.goto(x+20,y)
            turtle.setheading(90)
            turtle.forward(100)
            turtle.penup()
            turtle.goto(turtle.xcor()+tcircrad, turtle.ycor()+tcircrad)
            turtle.pendown()
            turtle.circle(tcircrad)
            turtle.penup()
            turtle.goto(k,l)
            turtle.pendown()
        if 'P' in n:
            turtle.goto(turtle.xcor()-20, turtle.ycor())
            turtle.setheading(90)
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(20)
            turtle.pen(fillcolor="black", pencolor="black", pensize=1)
            turtle.begin_fill()
            turtle.left(90)
            turtle.forward(15)
            turtle.right(150)
            turtle.forward(17.321)
            turtle.right(60)
            turtle.forward(17.321)
            turtle.right(150)
            turtle.forward(15)
            turtle.end_fill()
        turtle.penup()
        turtle.goto(x-((float(n[2]) - float(n[1]))/2), y-200)
        turtle.pendown()
        turtle.write(n[0], False, align="center", font=("Arial", 30, 'italic'))
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.penup()
        if a < len(orfs)-1:
            turtle.goto(x+(min(np.asarray(orfs[a+1][1:3])) - max(np.asarray(orfs[a][1:3]))),y)
        a += 1
        turtle.pendown()
    else:
        turtle.setheading(90)
        turtle.right(30)
        turtle.forward(115.47)
        turtle.right(150)
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(-(float(n[1]) - float(n[2]) - math.tan(math.radians(30)) * 100))
        turtle.left(90)
        turtle.forward(50)
        x,y = turtle.xcor(),turtle.ycor()
        print(x,y)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(-(float(n[1]) - float(n[2]) - math.tan(math.radians(30)) * 100))
        turtle.right(90)
        turtle.forward(50)
        turtle.right(150)
        turtle.forward(115.47)
        turtle.end_fill()
        k,l = turtle.xcor(),turtle.ycor()
        if 'T' in n:
            turtle.goto(turtle.xcor()-20,turtle.ycor())
            turtle.setheading(90)
            turtle.forward(100)
            turtle.penup()
            turtle.goto(turtle.xcor()+tcircrad, turtle.ycor()+tcircrad)
            turtle.pendown()
            turtle.circle(tcircrad)
            turtle.penup()
            turtle.goto(k,l)
            turtle.pendown()
        if 'P' in n:
            turtle.goto(turtle.xcor()+(max(n[1:3])-min(n[1:3]))+20, turtle.ycor())
            turtle.setheading(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(20)
            turtle.pen(fillcolor="black", pencolor="black", pensize=1)
            turtle.begin_fill()
            turtle.right(90)
            turtle.forward(15)
            turtle.left(150)
            turtle.forward(17.321)
            turtle.left(60)
            turtle.forward(17.321)
            turtle.left(150)
            turtle.forward(15)
            turtle.end_fill()
        turtle.penup()
        turtle.goto(x+((float(n[2]) - float(n[1]))/2), y-200)
        turtle.pendown()
        turtle.write(n[0], False, align="center", font=("Arial", 30, 'italic'))
        turtle.penup()
        turtle.goto(x, y)
        turtle.penup()
        if a < len(orfs)-1:
            turtle.goto(x-45,y)
        turtle.pendown()
        a += 1
turtle.done()

#save drawing as eps
#ts = turtle.getscreen()
#ts.getcanvas().postscript(file="test.eps")

