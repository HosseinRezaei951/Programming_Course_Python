import turtle
def drawLine(x1, y1, x2, y2):
    
    turtle.penup()
    turtle.goto(x1,y1)
    turtle.pendown()
    turtle.goto(x2,y2)
    turtle.penup()

def main():
    drawLine(-100, -100, 0, 100)
    drawLine(0, 100, 100, -100)
    drawLine(100, -100, -150, 50)
    drawLine(-150, 50, 150, 50)
    drawLine(150, 50, -100, -100)

main()
    
    
    
