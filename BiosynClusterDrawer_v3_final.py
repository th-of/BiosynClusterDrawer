# This draws biosynthetic clusters using the python turtle package
# import turtle
from turtle import *
import turtle
import math
import numpy as np
# from tkinter import *

# Fractional scaling value.
scale = 0.4

offset = -50 * scale
# Example input:
# [offset, ["label", start, stop, "color", "P"], ["label2", start, stop, "color", "P"]]
# Offset: length of sequence before the first ORF and after the last.
# Label: Name of gene/ORF, text to be added below.
# Start, stop: Real start and stop positions in the genome. 
# Color: "green", "red", "blue", "grey" etc.
# Promoters and terminators are identified by a string of "P" or "T" in the list of the reading frame with a 
# promoter ("P") upstream or a termintor ("T") downstream.
# P = promoter, T = terminator
gak = [-50, ["gakA", 4231, 4335, "blue", "P"], ["gakB", 4422, 4526, "blue"], ["gakC", 4561, 4659, "blue", "T"],  ["gakI", 5333, 4881, "red", "T"], ["cro", 5517, 5290, "grey", "P"], ["gakT", 5600, 7339, "green", "P", "T"]]

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
clusterlength = scale*(max(valsarray)+(2*abs(offset)))

## Scaling

for i in range(len(gak)):
    if type(gak[i]) is int:
        gak[i] = round(gak[i]*scale, 0)
    else:
        for n in range(len(gak[i])):
            if type(gak[i][n]) is int:
                gak[i][n] = round((gak[i][n])*scale, 0)
            

#Circle radius for terminator symbol
tcircrad = 15

# hide turtle and set draw speed

turtle.setup(width=2000, height=700, startx=0, starty=0)
turtle.screensize(2000, 700)
turtle.hideturtle()
turtle.speed(10)

# line
turtle.penup()
turtle.right(180)
turtle.forward(clusterlength*0.5)
turtle.right(180)
turtle.pendown()
turtle.pen(pencolor="black", pensize=2)
turtle.forward(clusterlength)

## draw orfs

turtle.penup()
turtle.right(180)
turtle.forward(clusterlength+offset)
a,b = turtle.xcor(), turtle.ycor()
print(a,b)
turtle.right(90)
turtle.pendown()
a = 0
for n in orfs:
    turtle.pen(fillcolor=n[3], pencolor="black", pensize=2)
    turtle.begin_fill()
    if n[1] < n[2]:
        turtle.setheading(90)
        turtle.forward(50*scale)
        turtle.right(90)
        turtle.forward((float(n[2]) - float(n[1]) - math.tan(math.radians(30)) * (100*scale)))
        turtle.left(90)
        turtle.forward(50*scale)
        turtle.right(150)
        turtle.forward((4*50*scale)*math.sin(math.radians(30)/math.sin(math.radians(120))))
        x,y = turtle.xcor(),turtle.ycor()
        turtle.right(60)
        turtle.forward((4*50*scale)*(math.sin(math.radians(30)/math.sin(math.radians(120)))))
        turtle.right(150)
        turtle.forward(50*scale)
        turtle.left(90)
        turtle.forward((float(n[2]) - float(n[1]) - math.tan(math.radians(30)) * (100*scale)))
        turtle.right(90)
        turtle.forward(50*scale)
        k,l = turtle.xcor(),turtle.ycor()
        turtle.end_fill()
        if 'T' in n:
            turtle.penup()
            turtle.goto(x+(20*scale),y)
            turtle.setheading(90)
            turtle.pendown()
            turtle.forward(100*scale)
            turtle.penup()
            turtle.goto(turtle.xcor()+(tcircrad*scale), turtle.ycor()+(tcircrad*scale))
            turtle.pendown()
            turtle.circle(tcircrad*scale)
            turtle.penup()
            turtle.goto(k,l)
            turtle.pendown()
        if 'P' in n:
            turtle.penup()
            turtle.goto(turtle.xcor()-(20*scale), turtle.ycor())
            turtle.setheading(90)
            turtle.pendown()
            turtle.forward(100*scale)
            turtle.right(90)
            turtle.forward(20*scale)
            turtle.pen(fillcolor="black", pencolor="black", pensize=1)
            turtle.begin_fill()
            turtle.left(90)
            turtle.forward(15*scale)
            turtle.right(150)
            turtle.forward(2*15*scale*0.568)
            turtle.right(60)
            turtle.forward(2*15*scale*0.568)
            turtle.right(150)
            turtle.forward(15*scale)
            turtle.end_fill()
        turtle.penup()
        turtle.goto(x-((float(n[2]) - float(n[1]))/2), y-(200*scale))
        turtle.pendown()
        turtle.write(n[0], False, align="center", font=("Arial", 15, 'italic'))
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
        turtle.forward((4*50*scale)*(math.sin(math.radians(30)/math.sin(math.radians(120)))))
        turtle.right(150)
        turtle.forward(50*scale)
        turtle.right(90)
        turtle.forward(-(float(n[1]) - float(n[2]) - math.tan(math.radians(30)) * (100*scale)))
        turtle.left(90)
        turtle.forward(50*scale)
        x,y = turtle.xcor(),turtle.ycor()
        print(x,y)
        turtle.forward(50*scale)
        turtle.left(90)
        turtle.forward(-(float(n[1]) - float(n[2]) - math.tan(math.radians(30)) * (100*scale)))
        turtle.right(90)
        turtle.forward(50*scale)
        turtle.right(150)
        turtle.forward((4*50*scale)*(math.sin(math.radians(30)/math.sin(math.radians(120)))))
        turtle.end_fill()
        k,l = turtle.xcor(),turtle.ycor()
        if 'T' in n:
            turtle.penup()
            turtle.goto(turtle.xcor()-(20*scale),turtle.ycor())
            turtle.setheading(90)
            turtle.pendown()
            turtle.forward(100*scale)
            turtle.penup()
            turtle.goto(turtle.xcor()+(tcircrad*scale), turtle.ycor()+(tcircrad*scale))
            turtle.pendown()
            turtle.circle(tcircrad*scale)
            turtle.penup()
            turtle.goto(k,l)
            turtle.pendown()
        if 'P' in n:
            turtle.penup()
            turtle.goto(turtle.xcor()+(max(n[1:3])-min(n[1:3]))+(20*scale), turtle.ycor())
            turtle.setheading(90)
            turtle.pendown()
            turtle.forward(100*scale)
            turtle.left(90)
            turtle.forward(20*scale)
            turtle.pen(fillcolor="black", pencolor="black", pensize=1)
            turtle.begin_fill()
            turtle.right(90)
            turtle.forward(15*scale)
            turtle.left(150)
            turtle.forward(2*15*scale*0.568)
            turtle.left(60)
            turtle.forward(2*15*scale*0.568)
            turtle.left(150)
            turtle.forward(15*scale)
            turtle.end_fill()
        turtle.penup()
        turtle.goto(x+((float(n[2]) - float(n[1]))/2), y-(200*scale))
        turtle.pendown()
        turtle.write(n[0], False, align="center", font=("Arial", 15, 'italic'))
        turtle.penup()
        turtle.goto(x, y)
        turtle.penup()
        if a < len(orfs)-1:
            turtle.goto(x+(min(np.asarray(orfs[a+1][1:3])) - max(np.asarray(orfs[a][1:3]))),y)
        turtle.pendown()
        a += 1
turtle.done()

#save drawing as eps
#ts = turtle.getscreen()
#ts.getcanvas().postscript(file="test.eps")

