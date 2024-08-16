import turtle

radius=eval(input("Enter the radius:"))

area=3.14159*(radius**2)

turtle.color("blue")
turtle.penup()
turtle.goto(0,-radius)
turtle.down()
turtle.circle(radius)

turtle.penup()
turtle.goto(0, 0)
turtle.write((int(area*100)/100))
turtle.hideturtle()

turtle.done()



