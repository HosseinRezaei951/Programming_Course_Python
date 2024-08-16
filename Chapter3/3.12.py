import turtle

length=eval(input("Enter the length of the star:"))

turtle.penup()
turtle.goto((length/4),-(length/4))
turtle.pendown()
turtle.left(108)
turtle.forward(length)

turtle.left(144)
turtle.forward(length)

turtle.left(144)
turtle.forward(length)

turtle.left(144)
turtle.forward(length)

turtle.left(144)
turtle.forward(length)

turtle.done()

