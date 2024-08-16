import math

x0,y0,x1,y1,x2,y2 = eval(input("Enter coordinates for the three points p0, p1, and p2: "))

R = ((x1 - x0)*(y2 - y0)) - ((x2 - x0)*(y1 - y0))

#Center of segment
X = (x0+x1)/2
Y = (y0+y1)/2

#distance : p2 VS Center of segment=(X,Y)
distance1 = math.sqrt( ((X-x2)**2)+((Y-y2)**2))

#distance : p1 VS Center of segment=(X,Y)
distance2 = math.sqrt( ((X-x0)**2)+((Y-y0)**2))

if ( ( R == 0 ) and ( distance1 <= distance2) )   :
            print("("+str(float(x2))+","+str(float(y2))+")",\
                  "is on the line segment from","("+str(float(x0))+","+str(float(y0))+")","to","("+str(float(x1))+","+str(float(y1))+")")

else  :
            print("("+str(float(x2))+","+str(float(y2))+")",\
                  "is not on the line segment from","("+str(float(x0))+","+str(float(y0))+")","to","("+str(float(x1))+","+str(float(y1))+")")
 
