number1 = eval(input("Plz enter the first number : "))
number2 = eval(input("Plz enter the second number : "))

if number2 < number1 :
    number1 , number2 = number2 , number1
    minimum = number1
else :
    minimum = number1


while minimum > 0 :
    
    if (number1 % minimum == 0) and (number2 % minimum == 0) :
        print("The greatest common divisor of two number is ", minimum)
        break

    elif minimum == 1 :
        print("The greatest common divisor of two number is 1 ")
        break
    
    minimum = minimum -  1
    

    

    
    

    
