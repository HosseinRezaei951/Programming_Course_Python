import turtle

radius=eval(input("Enter the radius:"))

turtle.color("red")
turtle.penup()
turtle.goto(radius,radius)
turtle.pendown()
turtle.circle(radius)


turtle.color("blue")
turtle.penup()
turtle.goto(-radius,radius)
turtle.pendown()
turtle.circle(radius)

turtle.color("red")
turtle.penup()
turtle.goto(-radius,-radius)
turtle.pendown()
turtle.circle(radius)


turtle.color("blue")
turtle.penup()
turtle.goto(radius,-radius)
turtle.pendown()
turtle.circle(radius)
turtle.done()



