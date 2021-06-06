"""
CELEBRATING PRIDE MONTH:

With the help of turtle library of Python, I made a simple python program to create a pride flag.
In this program, I defined a function to make a rectangle which is later used to create six rectangles
of different colors used to represent LBGTQ community.
"""

import turtle as tu      

#declaring background of the screen & coordinates of the turtle
tu.bgcolor("#ffb3b3")   
tu.speed(1)
tu.penup()
tu.goto(-200,200)
tu.pendown()

#defining a function 'rect' which is used to create a rectangle with dimensions x*y
def rect(x,y):
    tu.begin_fill()
    tu.forward(x)
    tu.left(90)
    tu.forward(y)
    tu.left(90)
    tu.forward(x)
    tu.left(90)
    tu.forward(y)
    tu.penup()
    tu.forward(y)
    tu.pendown()
    tu.end_fill()
    tu.left(90)    

#main program
tu.color("red")
rect(400,40)
tu.color("orange")
rect(400,40)
tu.color("yellow")
rect(400,40)
tu.color("green")
rect(400,40)
tu.color("blue")
rect(400,40)
tu.color("purple")
rect(400,40)
tu.hideturtle()
