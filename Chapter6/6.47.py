import turtle

def drawChessboard(startx, endx, starty, endy):
    turtle.setheading(45)
    A = 50
    
    for x in range(round(startx),round(endx),A):
        for y in range(starty,endy,A):
                turtle.penup()
                turtle.goto(x,y)
                turtle.pendown()
                turtle.begin_fill()
                turtle.pensize(1)
                turtle.pendown()
                turtle.circle((A/4*(2**0.5)),steps=4)
                turtle.end_fill()
                turtle.penup()
                
    for x in range(round(startx),round(endx),A):
        for y in range(starty,endy,A):
        
                turtle.goto(x+A/2,y-A/2)
                turtle.begin_fill()
                turtle.pensize(1)
                turtle.pendown()
                turtle.circle((A/4*2**0.5),steps=4)
                turtle.end_fill()
                turtle.penup()

def main():
    A = 50
    turtle.penup()
    turtle.goto(75-200,-125)
    turtle.pendown()
    turtle.goto(75-200,+75)
    turtle.left(90)
    turtle.goto(-125-200,75)
    turtle.left(90)
    turtle.goto(-125-200,-125)
    turtle.left(90)
    turtle.goto(+75-200,-125)
    drawChessboard(-300, -100, -100, 100)
    
    turtle.goto(75+200,-125)
    turtle.pendown()
    turtle.goto(75+200,+75)
    turtle.left(90)
    turtle.goto(-125+200,75)
    turtle.left(90)
    turtle.goto(-125+200,-125)
    turtle.left(90)
    turtle.goto(+75+200,-125)
    drawChessboard(-300+400, -100+400, -100, 100)

    turtle.hideturtle()
    

main()
