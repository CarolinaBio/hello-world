import turtle
amy = turtle.Turtle()
amy.color("yellow")
for side in [1, 2, 3, 4]:
    amy.forward(100)
    amy.right(90)
## this means that is just for your info, its not running anything 

    # General info:
    ## Import the turtle module.
import turtle

## Create a new turtle named amy.
amy = turtle.Turtle()

## Set amy's color.
amy.color("yellow")

## Have amy draw a square
amy.forward(100)
amy.right(90)
amy.forward(100)
amy.right(90)
amy.forward(100)
amy.right(90)
amy.forward(100)

# square qith different colors:
import turtle
amy = turtle.Turtle()

amy.color("red")
amy.forward(100)
amy.right(90)
amy.color("orange")
amy.forward(100)
amy.right(90)
amy.color("yellow")
amy.forward(100)
amy.right(90)
amy.color("green")
amy.forward(100)

# Loops: observe space 
import turtle
juno = turtle.Turtle()
juno.color("white")
# at least 4 spaces 
for side in [1,2,3]:
  #### juno.forward(100)
        juno.left(120)

#designating some_list as variable giving its value and using it for item..
import turtle
amy = turtle.Turtle()
amy.color("cyan")
some_list=[0,0,0,0,0,0,0,0,0,0,0,0]

for item in some_list:
    amy.forward(50)
    amy.right(30)

    angles;

import turtle

builder = turtle.Turtle()
builder.color("red")
builder.width(5)

angles = [-90, 0, 0, -90,
          135, 0, 0, 0, 
          90, 0, 0, 0,
          135, -90, 0, 0,
          90, 0, 0, 0]

for angle in angles:
    builder.right(angle)
    builder.forward(25)

#for nested loops: #loops inside Loops
#    for side in [1, 2, 3, 4]:
#        paul.forward(100)
#         paul.right(90)
#    for side in [1, 2, 3, 4]:
#        paul.forward(10)
#        paul.right(90)

#practice methods:
import turtle
amy = turtle.Turtle()
amy.width(10)
amy.penup()
amy.back(140)
amy.pendown()
amy.color("red")
amy.forward(50)
amy.penup()
amy.forward(50)
amy.pendown()
amy.color("orange")
amy.forward(50)
amy.penup()
amy.forward(50)
amy.pendown()
amy.color("yellow")
amy.forward(50)

import turtle
amy = turtle.Turtle()

# Make the width thicker so that the line will be easier to see
amy.width(5)

# Move back without drawing anything
amy.penup()
amy.forward(-140)
amy.pendown()

# Draw three shapes of different colors, with space in between
for prettycolor in ["red", "orange", "yellow"]:
    amy.color(prettycolor)
    for side in [1,2,3,4]:
      amy.forward(50)
      amy.right(90)
    amy.penup()
    amy.forward(100)
    amy.pendown()
