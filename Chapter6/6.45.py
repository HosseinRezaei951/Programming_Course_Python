import turtle

def drawPolygon(x = 0, y = 0, radius = 50, numberOfSides = 3):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.circle(50, steps = numberOfSides)



def main():
    drawPolygon(x = -250, y = 0, radius = 50, numberOfSides = 3)
    drawPolygon(x = -150, y = 0, radius = 50, numberOfSides = 4)
    drawPolygon(x = -50, y = 0, radius = 50, numberOfSides = 5)
    drawPolygon(x = 50, y = 0, radius = 50, numberOfSides = 6)
    drawPolygon(x = 150, y = 0, radius = 50, numberOfSides = 7)
    drawPolygon(x = 250, y = 0, radius = 50, numberOfSides = 8)


main()
