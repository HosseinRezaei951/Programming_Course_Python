import turtle

turtle.begin_fill()
turtle.color("red")
turtle.penup()
turtle.goto(100,0)

turtle.pendown()
turtle.left(90)

turtle.circle(100,steps=6)

turtle.end_fill()

turtle.color("black")
turtle.pensize(5)
turtle.circle(100,steps=6)

turtle.color("white")
turtle.penup()
turtle.goto(-88,-38)
turtle.right(90)
turtle.pendown()
turtle.write("STOP",font=("Arial Black",45, "bold"))




