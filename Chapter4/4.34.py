x = ord(input("Enter a hex character: "))

if ( 48 <= x <= 57 ) :
            x1 = x - 48
            print("The decimal value is",x1)

            
elif ( 97 <= x <= 102 ) :
            x1 = x - 87
            print("The decimal value is",x1)
           
            
elif ( 65 <= x <= 70 ) :
            x1 = x - 55
            print("The decimal value is",x1)

elif ( (not( 65 <= x <= 70 )) or (not( 97 <= x <= 102 )) or(not( 48 <= x <= 57 )) ):
            print("Invalid input")

            
            
