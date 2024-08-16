import turtle

x,y = eval(input("Enter a point (Ex:(x, y)): "))

x0,y0 = 0 , 0
w,h = 100 , 50

if ( abs(x) <= 50 and abs(y) <= 25 ) :

            turtle.penup()
            turtle.goto(50,0)
            turtle.pendown()
            turtle.left(90)
            turtle.forward(25)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(50)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(25)

            turtle.penup()
            turtle.goto(x+3,y)
            turtle.begin_fill()
            turtle.color("red")
            turtle.circle(3)
            turtle.end_fill()

            turtle.penup()
            turtle.goto((-(w+50)),(-(h+20)))
            turtle.write("The point is inside the rectangle",font=("Aharoni",16,"bold"))
            turtle.hideturtle()

else :
            turtle.penup()
            turtle.goto(50,0)
            turtle.pendown()
            turtle.left(90)
            turtle.forward(25)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(50)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(25)

            turtle.penup()
            turtle.goto(x+3,y)
            turtle.begin_fill()
            turtle.color("red")
            turtle.circle(3)
            turtle.end_fill()

            turtle.penup()
            turtle.goto((-(w+50)),(-(h+20)))
            turtle.write("The point is outside the rectangle",font=("Aharoni",16,"bold"))
            turtle.hideturtle()
            
                        

            
            
            
