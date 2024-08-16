import math

x,y = eval(input("Enter a point's x- and y-coordinates: "))

#A :
x1,y1 = 0 , 100

#B :
x2,y2 = 200 , 0

#C :
x0,y0 = 0 , 0

#tan(b) :
EX = (y2-y1)/(x2-x1)
TRY = (y2-y)/(x2-x)

if ( ( x < 0 ) or (( x > 0 ) and ( y < 0 )) ) :
            print("The point is not in the triangle")

elif ( x == 200 and y == 0 ) :
            print("The point is in the triangle")

elif ( TRY >= EX ) :
            print("The point is in the triangle")

elif ( not( TRY >= EX ) ) :
            print("The point is not in the triangle")


