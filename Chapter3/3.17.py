import turtle
import math

x1,y1=eval(input("enter the three points (p1) for a triangle:"))

x2,y2=eval(input("enter the three points (p2) for a triangle:"))

x3,y3=eval(input("enter the three point3 (p3) for a triangle:"))

side1=math.sqrt(pow((x2-x1),2)+pow((y2-y1),2))
side2=math.sqrt(pow((x2-x3),2)+pow((y2-y3),2))
side3=math.sqrt(pow((x3-x1),2)+pow((y3-y1),2))

s=(side1+side2+side3)/2

area=math.sqrt((s*(s-side1)*(s-side2)*(s-side3)))

turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.write('p1'+'('+str(x1)+str(y1)+')')
turtle.goto(x2,y2)
turtle.write('p2'+'('+str(x2)+str(y2)+')')
turtle.goto(x3,y3)
turtle.write('p3'+'('+str(x3)+str(y3)+')')
turtle.goto(x1,y1)

turtle.penup()
turtle.goto(x2,(y2-25))
turtle.write('The area of triangle is '+str(area))








