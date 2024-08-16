import turtle

x0,y0,x1,y1,x2,y2 = eval(input("Enter coordinates for the three points p0, p1, and p2: "))

R = ((x1 - x0)*(y2 - y0)) - ((x2 - x0)*(y1 - y0))

if ( R > 0 ) :
            turtle.penup()
            turtle.goto(x0,y0)
            p1 = 'p1('+str(x0)+','+str(y0)+')'
            turtle.write(p1)
            turtle.pendown()
            turtle.goto(x1,y1)
            turtle.penup()
            p2 = 'p2('+str(x1)+','+str(y1)+')'
            turtle.write(p2)

            turtle.penup()
            turtle.goto(0,0)
            turtle.goto(x2,y2-3)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(3)
            turtle.end_fill()
            turtle.penup()
            X,Y = (x2-100),(y2-20)
            turtle.goto(X,Y)
            turtle.write("p2 is on the left side of the line from p1 to p2")
            turtle.hideturtle()

            
elif ( R == 0 ) :
            turtle.penup()
            turtle.goto(x0,y0)
            p1 = 'p1('+str(x0)+','+str(y0)+')'
            turtle.write(p1)
            turtle.pendown()
            turtle.goto(x1,y1)
            turtle.penup()
            p2 = 'p2('+str(x1)+','+str(y1)+')'
            turtle.write(p2)

            turtle.penup()
            turtle.goto(0,0)
            turtle.goto(x2,y2-3)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(3)
            turtle.end_fill()
            turtle.penup()
            X,Y = (x2-100),(y2-20)
            turtle.goto(X,Y)
            turtle.write("p2 is on the same line from p1 to p2")
            turtle.hideturtle()

elif ( R < 0 ) :
            turtle.penup()
            turtle.goto(x0,y0)
            p1 = 'p1('+str(x0)+','+str(y0)+')'
            turtle.write(p1)
            turtle.pendown()
            turtle.goto(x1,y1)
            turtle.penup()
            p2 = 'p2('+str(x1)+','+str(y1)+')'
            turtle.write(p2)

            turtle.penup()
            turtle.goto(0,0)
            turtle.goto(x2,y2-3)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(3)
            turtle.end_fill()
            turtle.penup()
            X,Y = (x2-100),(y2-20)
            turtle.goto(X,Y)
            turtle.write("p2 is on the right side of the line from p1 to p2")
            turtle.hideturtle()
