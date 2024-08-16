import math

#Charlotte
X1,Y1=35.2270869,-80.8431267

#Atlanta
X2,Y2=33.7489954,-84.3879824

#Orlando
X3,Y3=28.5383355,-81.3792365

#Savannah
X4,Y4=32.0835407,-81.0998342


x2,y2=math.radians(X2),math.radians(Y2)

x3,y3=math.radians(X3),math.radians(Y3)

x4,y4=math.radians(X4),math.radians(Y4)

x1,y1=math.radians(X1),math.radians(Y1)

                                    
#TR1
Charlotte_to_Atlanta=6371.01* (math.acos((math.sin(x2) * math.sin(x1)) + (math.cos(x2) * math.cos(x1) * math.cos(y1 - y2))))

Charlotte_to_Savannah=6371.01* (math.acos((math.sin(x4) * math.sin(x1)) + (math.cos(x4) * math.cos(x1) * math.cos(y1 - y4))))

Savannah_to_Atlanta=6371.01* (math.acos((math.sin(x2) * math.sin(x4)) + (math.cos(x2) * math.cos(x4) * math.cos(y4 - y2))))



#TR2
Orlando_to_Atlanta=6371.01* (math.acos((math.sin(x3) * math.sin(x2)) + (math.cos(x3) * math.cos(x2) * math.cos(y2 - y3))))

Orlando_to_Savannah=6371.01* (math.acos((math.sin(x3) * math.sin(x4)) + (math.cos(x3) * math.cos(x4) * math.cos(y4 - y3))))

Savannah_to_Atlanta=6371.01* (math.acos((math.sin(x2) * math.sin(x4)) + (math.cos(x2) * math.cos(x4) * math.cos(y4 - y2))))


#compute area1
s1=(Charlotte_to_Atlanta+Charlotte_to_Savannah+Savannah_to_Atlanta)/2

area1=(s1*(s1-Charlotte_to_Atlanta)*(s1-Charlotte_to_Savannah)*(s1-Savannah_to_Atlanta))**(0.5)


#compute area2
s2=(Orlando_to_Atlanta+Orlando_to_Savannah+Savannah_to_Atlanta)/2

area2=(s2*(s2-Orlando_to_Atlanta)*(s2-Orlando_to_Savannah)*(s2-Savannah_to_Atlanta))**(0.5)


Tarea=area1+area2

print("Area is",Tarea)
