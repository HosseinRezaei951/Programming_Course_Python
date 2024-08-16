import turtle
import math

x1,y1,w1,h1 = eval(input("Enter r1's center x-, y-coordinates, width, and height: "))
x2,y2,w2,h2 = eval(input("Enter r2's center x-, y-coordinates, width, and height: "))

H = abs(y1 - y2)
W = abs(x1 - x2)

#Scale width 
Scale1 = abs((w1/2)-(w2/2))
Scale1_2 = (w1/2)+(w2/2)

#Scale height 
Scale2 = abs((h1/2)-(h2/2))
Scale2_2 = (h1/2)+(h2/2)


if ( (W <= Scale1) and (H <= Scale2) ) :
            
            turtle.penup()
            turtle.goto((x1+(w1/2)),y1)
            turtle.pendown()
            turtle.left(90)
            turtle.forward(h1/2)
            turtle.left(90)
            turtle.forward(w1)
            turtle.left(90)
            turtle.forward(h1)
            turtle.left(90)
            turtle.forward(w1)
            turtle.left(90)
            turtle.forward(h1/2)

            turtle.penup()
            turtle.goto(0,0)
            turtle.goto((x2+(w2/2)),y2)
            turtle.pendown()
            
            turtle.forward(h2/2)
            turtle.left(90)
            turtle.forward(w2)
            turtle.left(90)
            turtle.forward(h2)
            turtle.left(90)
            turtle.forward(w2)
            turtle.left(90)
            turtle.forward(h2/2)

            turtle.write("r2 is inside r1",font=("Aharoni",32,"bold"))
            turtle.hideturtle()

            
            
elif ( (W > Scale1_2) or (H > Scale2_2) ) :

            turtle.penup()
            turtle.goto((x1+(w1/2)),y1)
            turtle.pendown()
            turtle.left(90)
            turtle.forward(h1/2)
            turtle.left(90)
            turtle.forward(w1)
            turtle.left(90)
            turtle.forward(h1)
            turtle.left(90)
            turtle.forward(w1)
            turtle.left(90)
            turtle.forward(h1/2)

            turtle.penup()
            turtle.goto(0,0)
            turtle.goto((x2+(w2/2)),y2)
            turtle.pendown()
            
            turtle.forward(h2/2)
            turtle.left(90)
            turtle.forward(w2)
            turtle.left(90)
            turtle.forward(h2)
            turtle.left(90)
            turtle.forward(w2)
            turtle.left(90)
            turtle.forward(h2/2)

            turtle.write("r2 does not overlap r1",font=("Aharoni",32,"bold"))
            turtle.hideturtle()
            
            

elif ( ( (W > Scale1) and (H > Scale2) ) or (W > Scale1) or (H > Scale2) ) :

            turtle.penup()
            turtle.goto((x1+(w1/2)),y1)
            turtle.pendown()
            turtle.left(90)
            turtle.forward(h1/2)
            turtle.left(90)
            turtle.forward(w1)
            turtle.left(90)
            turtle.forward(h1)
            turtle.left(90)
            turtle.forward(w1)
            turtle.left(90)
            turtle.forward(h1/2)

            turtle.penup()
            turtle.goto(0,0)
            turtle.goto((x2+(w2/2)),y2)
            turtle.pendown()
            
            turtle.forward(h2/2)
            turtle.left(90)
            turtle.forward(w2)
            turtle.left(90)
            turtle.forward(h2)
            turtle.left(90)
            turtle.forward(w2)
            turtle.left(90)
            turtle.forward(h2/2)

            turtle.write("r2 overlaps r1",font=("Aharoni",32,"bold"))
            turtle.hideturtle()
     
            



