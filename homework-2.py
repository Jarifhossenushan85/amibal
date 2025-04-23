import turtle

def draw_equilateral_triangle():
    turtle.color("blue")
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(100)  # Length of each side
        turtle.left(120)     # Angle for equilateral triangle
    turtle.end_fill()

def draw_rectangle():
    turtle.color("green")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(150)  # Length of the longer side
        turtle.left(90)
        turtle.forward(100)  # Length of the shorter side
        turtle.left(90)
    turtle.end_fill()

def draw_hexagon():
    turtle.color("purple")
    turtle.begin_fill()
    for _ in range(6):
        turtle.forward(100)  # Length of each side
        turtle.left(60)      # Angle for hexagon
    turtle.end_fill()

# Main program
turtle.speed(3)  # Set the drawing speed
turtle.bgcolor("lightyellow")  # Set background color

# Draw the shapes
draw_equilateral_triangle()
turtle.penup()
turtle.goto(-200, 0)  # Move to a new position for the rectangle
turtle.pendown()
draw_rectangle()
turtle.penup()
turtle.goto(200, 0)  # Move to a new position for the hexagon
turtle.pendown()
draw_hexagon()

# Finish
turtle.done()
