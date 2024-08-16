import turtle
import math

def drawLine(x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)

def writeText(s, x, y):
    turtle.penup() 
    turtle.goto(x, y)
    turtle.pendown() 
    turtle.write(s)

def main():
    # X
    drawLine(-200, 0, 200, 0)
    drawLine(200, 0, 185, -5)
    drawLine(200, 0, 185, +5)
    writeText("X", 201, 0)
    
    # Y
    drawLine(0, - 2*(50 * math.sin((-175/ 100) * 2 * math.pi)), 0, 2*(50 * math.sin((-175/ 100) * 2 * math.pi)))
    drawLine(0, + 2*(50 * math.sin((-175/ 100) * 2 * math.pi)), 5, (2*(50 * math.sin((-175/ 100) * 2 * math.pi)))-15)
    drawLine(0, + 2*(50 * math.sin((-175/ 100) * 2 * math.pi)), -5, (2*(50 * math.sin((-175/ 100) * 2 * math.pi)))-15)
    writeText("Y", 0, (2*(50 * math.sin((-175/ 100) * 2 * math.pi)))+1)

    # sin
    turtle.penup()
    for x in range(-175, 176):
        turtle.goto(x, 50 * math.sin((x / 100) * 2 * math.pi))
        turtle.pendown()
    # cos
    turtle.penup()
    for x in range(-175, 176):
        turtle.goto(x, 50 * math.cos((x / 100) * 2 * math.pi))
        turtle.pendown()

    writeText("2\u03c0", -100, -15)
    writeText("-2\u03c0", 100, -15)
    

    
main()
    

    
    
