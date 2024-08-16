import turtle
turtle.speed(10)
for n in range(1,11):
    i = n
    turtle.penup()
    turtle.goto(0,-10*n)
    turtle.pendown()
    turtle.circle(10*n)
    
