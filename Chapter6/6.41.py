import turtle
import random
def drawCircle(x = 0, y = 0, radius = 10):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.circle(radius)

def drawRectangle(x = 0, y = 0, width = 10, height = 10):
    turtle.penup()
    turtle.goto(x + width / 2, y + height / 2)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)

def drawPoint(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(3)
    turtle.end_fill()

def main():
    drawCircle(x = 50, y = 0, radius = 50)
    drawRectangle(x = -75, y = 0, width = 100, height = 100)
    for i in range(1,11):
        x = random.randint(-120,-20)
        y = random.randint(-45,45)
        drawPoint(x, y)
        
    counter = 0
    x = 1
    y = 1
    flag = False
    while flag == False :
        x = random.randint(5,95)
        y = random.randint(-45,45)
        d = (((x - 50) **2) + ((y - 0) **2)) ** 0.5
        if d < 50 and counter < 10  :
            drawPoint(x, y)
            counter += 1
        if counter == 10 :
            flag = True

    
        

main()
    

