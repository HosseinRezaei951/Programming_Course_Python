import turtle
import math

x1,y1=eval(input("enter the three points (p1) for a triangle:"))

x2,y2=eval(input("enter the three points (p2) for a triangle:"))

x3,y3=eval(input("enter the three point3 (p3) for a triangle:"))

a=math.sqrt((x2-x3)*(x2-x3)+(y2-y3)*(y2-y3))
b=math.sqrt((x1-x3)*(x1-x3)+(y1-y3)*(y1-y3))
c=math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))

A=math.degrees(math.acos((a * a - b * b - c * c) / (-2 * b * c)))
B=math.degrees(math.acos((b * b - a * a - c * c) / (-2 * a * c)))
C=math.degrees(math.acos((c * c - b * b - a * a) / (-2 * a * b)))

turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.write('p1'+'('+str((int(A*100))/100)+')')
turtle.goto(x2,y2)
turtle.write('p2'+'('+str((int(B*100))/100)+')')
turtle.goto(x3,y3)
turtle.write('p3'+'('+str((int(C*100))/100)+')')
turtle.goto(x1,y1)











