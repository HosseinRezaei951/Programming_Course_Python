x1,y1,x2,y2,x3,y3,x4,y4 = eval(input("Enter x1, y1, x2, y2, x3, y3, x4, y4: "))

#1
a = y1 - y2
b = x1 - x2
e = ((a) * x1) - ((b) * y1)

#2
c = y3 - y4
d = x3 - x4
f = ((c) * x3) - ((d) * y3)


if  ( ((c*b)-(d*a))!=0 ):

            X = ( ((b*f)-(e*d)) / ((b*c)-(a*d)) )
            Y = ( ((f*a)-(e*c)) / ((c*b)-(d*a)) )
            print("The intersecting point is at",'(' , format(X,".5f") , ',' , format(Y,".5f") ,')')

elif  ( ((c*b)-(d*a))==0 ):
            print("The two lines are parallel")
 
