import math

x,y = eval(input("Enter a point with two coordinates( Ex:(x, y) ): "))


if (( x < (10/2) ) and ( y < (5.0/2) ))  :
            print("Point" + '(' + str(float(x)) + ',' + str(float(y)) + ')' + "is in the rectangle")

elif (( x > (10/2) ) or ( y > (5.0/2) )) :
            print("Point" + '(' + str(float(x)) + ',' + str(float(y)) + ')' + "is not in the rectangle")

elif ((( x == (10/2) ) or ( y == (5.0/2) )) or\
      (( x == (10/2) ) and ( y == (5.0/2) ))) :
            print("Point" + '(' + str(float(x)) + ',' + str(float(y)) + ')' + "on the rectangle")
