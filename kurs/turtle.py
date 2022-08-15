# import turtle

# screen = turtle.Screen()
# screen.setup(500,500)

# tu = turtle.Turtle()
# for i in range(10):
#     tu.forward(100)
#     tu.left(45)

import turtle

screen = turtle.Screen()
screen.setup(500,500)

tu = turtle.Turtle()
tu.shape('turtle')
tu.pencolor('red')
n = 6
for i in range(n):
    tu.forward(100)
    tu.left(360/n)
tu.up()
tu.goto(0, -100)
tu.setheading(90)
screen.exitonclick()