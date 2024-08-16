import turtle
import math

turtle.pendown()
turtle.forward(175)

turtle.right(150)
turtle.forward(15)
turtle.backward(15)

turtle.left(300)
turtle.forward(15)
turtle.backward(15)

turtle.right(150)
turtle.backward(2*175)

turtle.penup()
turtle.goto(0, - 2*(50 * math.sin((-175/ 100) * 2 * math.pi)))
turtle.pendown()
turtle.goto(0,2*( 50 * math.sin((-175/ 100) * 2 * math.pi)))

turtle.right(60)
turtle.forward(15)
turtle.backward(15)

turtle.left(300)
turtle.forward(15)
turtle.backward(15)


turtle.penup()
turtle.goto(-175, 50 * math.sin((-175/ 100) * 2 * math.pi))
turtle.pendown()
for x in range(-175, 176):
    turtle.goto(x, 50 * math.sin((x / 100) * 2 * math.pi))


turtle.penup()
turtle.goto(100, -15)
turtle.pendown()
turtle.write("2\u03c0")

turtle.penup()
turtle.goto(-100, -15)
turtle.pendown()
turtle.write("-2\u03c0")
turtle.hideturtle()



