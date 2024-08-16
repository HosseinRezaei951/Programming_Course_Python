import math

r=eval(input("Enter the length from the center to a vertex:"))

s=2*r*math.sin(math.pi/5)

area=(3*math.sqrt(3)*pow(s,2))/2

end=format(area,".2f")

print("The area of the pentagon is",end)
