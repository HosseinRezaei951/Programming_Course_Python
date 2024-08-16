import turtle
import random
import math

x1,y1 = eval(input("Enter the center of circle (Ex : x,y): "))
radius = eval(input("Enter the radius of circle : "))

x2=random.randint((-radius),(radius))
y2=random.randint((-radius),(radius))

Distance = math.sqrt( ((x2-x1)**2)+((y2-y1)**2) )

if ( Distance <= radius ) :
            turtle.penup()
            turtle.goto(x1,y1-radius)
            turtle.pendown()
            turtle.circle(radius)

            turtle.penup()
            turtle.goto(((x1+x2)-3),(y1+y2))
            turtle.pendown()
            turtle.begin_fill()
            turtle.color("red")
            turtle.circle(3)
            turtle.end_fill()

            turtle.penup()
            turtle.goto(x1-120,(y1-(radius+50)))
            turtle.pendown()
            turtle.write("The point is inside the circle",font=("Aharoni",16,"bold"))
            turtle.hideturtle()

else :
            
            turtle.penup()
            turtle.goto(x1,y1-radius)
            turtle.pendown()
            turtle.circle(radius)

            turtle.penup()
            turtle.goto(((x1+x2)-3),(y1+y2))
            turtle.pendown()
            turtle.begin_fill()
            turtle.color("red")
            turtle.circle(3)
            turtle.end_fill()

            turtle.penup()
            turtle.goto(x1-120,(y1-(radius+50)))
            turtle.pendown()
            turtle.write("The point is outside the circle",font=("Aharoni",16,"bold"))
            turtle.hideturtle()



            
