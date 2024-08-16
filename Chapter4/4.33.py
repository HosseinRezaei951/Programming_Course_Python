x = eval(input("Enter a decimal value (0 to 15): "))

if ( 0 <= x <= 9 ) :
            print("The hex value is",x)

elif (x == 10):
            print("The hex value is A")
            
elif (x == 11):
            print("The hex value is B")
            
elif (x == 12):
            print("The hex value is C")
            
elif (x == 13):
            print("The hex value is D")
            
elif (x == 14):
            print("The hex value is E")
            
elif (x == 15):
            print("The hex value is F")

else :
            print("Invalid input")
