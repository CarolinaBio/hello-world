# hello-world
this is a repository for practicing github
#this is the main,  main and readme-edits. Right now, they look exactly the same. Next you'll add changes to the new readme-edits branch.

import turtle
terry=turtle.Turtle()
terry.width(5)
terry.speed(0)
for side in [1,2,3,4,5,6]:
    rainbow = ["red", "orange", "yellow", "green", "blue", "purple"]
    terry.forward(60)
    terry.right(60)
    terry.color(rainbow[side])


import turtle
rainbow = ["yellow", "blue", "pink", "red"]
terry=turtle.Turtle()
terry.width(5)
terry.speed(0)
terry.penup()
terry.back(50)
terry.pendown()
for pretty_color in rainbow:
    terry.color(pretty_color)
    terry.forward(100)
    terry.right(90)
    for side in[5,6,7,8]:
             terry.forward(10)
             terry.right(90)

import turtle

rainbow = ["red", "orange", "yellow", "green", "blue", "purple"]

# Write whatever code you want here!
terry = turtle.Turtle()
terry.width(5)
terry.penup()
terry.back(50)
terry.pendown()
for pretty_color in rainbow:
    terry.color(pretty_color)
    terry.forward(100)
    terry.right(60)
terry.hideturtle()

#stars of each color
import turtle

rainbow = ["red", "orange", "yellow", "green", "blue", "purple"]

stars = turtle.Turtle()
stars.width(5)
stars.speed(0)
for color in rainbow:
    stars.color(color)
    for side in [1, 2, 3, 4, 5]:
        stars.forward(50)
        stars.right(144)
    stars.right(60)
    stars.penup()
    stars.forward(50)
    stars.pendown()
#Lesson Recap
Here's a more detailed outline of the main topics in this lesson. If you followed along with everything, you've now learned how to:

Use the turtle module to draw shapes.
Define variables and use them in place of hard-coded constants.
Use fundamental data types (including strings, lists, and integers).
Import modules from the Python standard library.
Use methods to control the behavior of Python objects.
Use comments to add documentation to code and activate/de-activate code.
Use a for loop to iterate over a data structure.
Use a loop variable to generate a result that changes each time a for loop runs.
Use a nested for loop in Python and correctly predict the number of times the nested loop will run.
Recognize and fix common errors.
Write compound statements and use indentation to indicate when code belongs to a given block.
