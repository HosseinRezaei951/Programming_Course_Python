A,B,C = eval(input("Enter three edges: "))

if (A > 0 and B > 0 and C > 0 ):

            if ( (A < B+C) and (B < A+C) and (C < A+B) ):
                        perimeter = A+B+C
                        print ("The perimeter is ",perimeter)

            if ( (not(A < B+C)) or (not(B < A+C)) or (not(C < A+B)) ):
                        perimeter = A+B+C
                        print ("The input is invalid")
                        
if (A <= 0 or B <= 0 or C <= 0 ):
             print ("The input is invalid")
            
            
