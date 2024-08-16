import turtle


radius=eval(input("Enter the radius of the rings:"))

turtle.pensize(5)
turtle.circle(radius)

turtle.color("red")
turtle.penup()
turtle.goto((2*radius)+10,0)
turtle.pendown()
turtle.circle(radius)

turtle.color("blue")
turtle.penup()
turtle.goto(-((2*radius)+10),0)
turtle.pendown()
turtle.circle(radius)

turtle.color("yellow")
turtle.penup()
turtle.goto(-(radius+10),-(radius))
turtle.pendown()
turtle.circle(radius)

turtle.color("green")
turtle.penup()
turtle.goto((radius+10),-(radius))
turtle.pendown()
turtle.circle(radius)

turtle.hideturtle()




