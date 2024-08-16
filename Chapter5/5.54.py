import turtle
import math

turtle.pendown()
turtle.forward(210)

turtle.right(150)
turtle.forward(15)
turtle.backward(15)

turtle.left(300)
turtle.forward(15)
turtle.backward(15)
turtle.write("X",font=(24))

turtle.right(150)
turtle.backward(2*210)


turtle.penup()
turtle.goto(0,-175)
turtle.pendown()
turtle.goto(0,175)

turtle.right(60)
turtle.forward(15)
turtle.backward(15)

turtle.left(300)
turtle.forward(15)
turtle.backward(15)
turtle.write("Y",font=(24))

turtle.penup()
turtle.goto(0,0)


for x in range(-120,121,3):
    turtle.goto(x,(x**2)/100)
    turtle.pendown()

turtle.hideturtle()
