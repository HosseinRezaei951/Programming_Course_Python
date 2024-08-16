import turtle

X,Y,width,height=eval(input("enter the center of a rectangle(EX:x,y), width, and height:"))

turtle.penup()

turtle.goto(X+(width/2),Y)
turtle.pendown()

turtle.left(90)
turtle.forward(height/2)

turtle.left(90)
turtle.forward(width)

turtle.left(90)
turtle.forward(height)

turtle.left(90)
turtle.forward(width)

turtle.left(90)
turtle.forward(height/2)

turtle.hideturtle()


