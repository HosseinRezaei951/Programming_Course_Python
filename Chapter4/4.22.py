import math

x,y = eval(input("Enter a point with two coordinates( Ex:(x, y) ): "))

X,Y = 0,0

distance = math.sqrt( ((x -X)**2) + ((y -Y)**2) )

if distance < 10 :
            print("Point" + '(' + str(float(x)) + ',' + str(float(y)) + ')' + "is in the circle")

elif distance > 10 :
            print("Point" + '(' + str(float(x)) + ',' + str(float(y)) + ')' + "is not in the circle")

elif distance == 10 :
            print("Point" + '(' + str(float(x)) + ',' + str(float(y)) + ')' + "on the circle")
