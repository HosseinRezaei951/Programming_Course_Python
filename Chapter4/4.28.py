import math 

x1,y1,w1,h1 = eval(input("Enter r1's center x-, y-coordinates, width, and height: "))
x2,y2,w2,h2 = eval(input("Enter r2's center x-, y-coordinates, width, and height: "))

H = abs(y1 - y2)
W = abs(x1 - x2)

#Scale width 
Scale1 = abs((w1/2)-(w2/2))
Scale1_2 = (w1/2)+(w2/2)

#Scale height 
Scale2 = abs((h1/2)-(h2/2))
Scale2_2 = (h1/2)+(h2/2)


if ( (W <= Scale1) and (H <= Scale2) ) :
            print("r2 is inside r1")
            
elif ( (W > Scale1_2) or (H > Scale2_2) ) :
            print("r2 does not overlap r1")
            

elif ( ( (W > Scale1) and (H > Scale2) ) or (W > Scale1) or (H > Scale2) ) :
     
            print("r2 overlaps r1")



