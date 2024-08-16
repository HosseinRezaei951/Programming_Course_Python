import math

#prompts the user to enter values for a, b, and c
a,b,c = eval(input("Enter a, b, c:"))

#compute the discriminant of the quadratic equation
discriminant = ((pow(b,2))-(4*a*c))

#campute the answers
    

if discriminant > 0 :
      print("The roots are",((int(r1*1000000))/1000000),"and",((int(r2*100000))/100000))

elif discriminant == 0 :
      print("The roots is",r3)
      
elif discriminant < 0 :
      print("The equation has no real roots.")
      




