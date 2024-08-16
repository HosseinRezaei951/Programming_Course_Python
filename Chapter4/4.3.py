import math

#prompts the user to enter a, b, c, d, e, and f
a , b , c , d , e , f = eval(input(" Enter a, b, c, d, e, f to solve 2*2 linear equations : "))

#compute x and y :
x = ((e*d)-(b*f))/((a*d)-(b*c))
y = ((a*f)-(e*c))/((a*d)-(b*c))

#display the result
if ((a*d)-(b*c)) == 0 :
    print("The equation has no solution")
    
else:
      print("x is",x,"and y is",y)
