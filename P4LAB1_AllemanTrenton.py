# Trenton Alleman
# 11/02/2025
# P4LAB1
# Using a turtle graphics program and a loop to draw a triangle and a square.

import turtle

# Creating the turtle window and drawing object
win = turtle.Screen()
pen = turtle.Turtle()

# Setting the turtle options
pen.pensize(5)
pen.pencolor("purple")
pen.shape("arrow")

# Code to draw the sqaure
for side in range(4) :
    pen.forward(200)
    pen.left(90)

# Code to draw the triangle
sides = 0

while sides < 3:
    pen.forward(200)
    pen.left(120)
    sides = sides + 1



# Wait for user to close the window
win.mainloop()