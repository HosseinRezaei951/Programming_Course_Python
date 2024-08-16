import math

x1,y1,r1=eval(input("Enter circle1's center x-, y-coordinates, and radius: "))
x2,y2,r2=eval(input("Enter circle2's center x-, y-coordinates, and radius: "))

between_the_two_centers = math.sqrt( ((x1-x2)**2)+((y2-y1)**2) )



if ( between_the_two_centers <= (abs(r1-r2)) ) :
            print("circle2 is inside circle1")

elif ( between_the_two_centers <= (r1+r2) ) :
            print("circle2 overlaps circle1")

else :
            
            print("circle2 does not overlap circle1")


