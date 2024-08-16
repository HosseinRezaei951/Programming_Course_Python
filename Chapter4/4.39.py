import math
import turtle

x1,y1,r1=eval(input("Enter circle1's center x-, y-coordinates, and radius: "))
x2,y2,r2=eval(input("Enter circle2's center x-, y-coordinates, and radius: "))

between_the_two_centers = math.sqrt( ((x1-x2)**2)+((y2-y1)**2) )



if ( between_the_two_centers <= (abs(r1-r2)) ) :
            
            turtle.penup()
            turtle.goto(x1,y1)
            turtle.goto(x1+r1,y1)
            turtle.pendown()
            turtle.circle(r1)

            turtle.penup()
            turtle.goto(0,0)
            turtle.goto(x2,y2)
            turtle.goto(x2+r2,y2)
            turtle.pendown()
            turtle.circle(r2)

            turtle.write("circle2 is inside circle1",font=("Aharoni",16,"bold"))
            

elif ( between_the_two_centers <= (r1+r2) ) :

            turtle.penup()
            turtle.goto(x1,y1)
            turtle.goto(x1+r1,y1)
            turtle.pendown()
            turtle.circle(r1)

            turtle.penup()
            turtle.goto(0,0)
            turtle.goto(x2,y2)
            turtle.goto(x2+r2,y2)
            turtle.pendown()
            turtle.circle(r2)

            turtle.write("circle2 overlaps circle1",font=("Aharoni",16,"bold"))
            

else :
            
            turtle.penup()
            turtle.goto(x1,y1)
            turtle.goto(x1+r1,y1)
            turtle.pendown()
            turtle.circle(r1)

            turtle.penup()
            turtle.goto(0,0)
            turtle.goto(x2,y2)
            turtle.goto(x2+r2,y2)
            turtle.pendown()
            turtle.circle(r2)

            turtle.write("circle2 does not overlap circle1",font=("Aharoni",16,"bold"))
            



