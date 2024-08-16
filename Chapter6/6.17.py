def isValid(side1, side2, side3):
    
    if side1+side2 > side3 and \
       side1+side3 > side2 and \
       side2+side3 > side1 :
        
        return True
    else :
        return False

def area(side1, side2, side3):
    
    s = (side1 + side2 + side3) / 2
    
    area = (s*(s - side1)*(s - side2)*(s - side3))**0.5
    print()
    print("The area of the triangle is ",area)

def main():
    side1 , side2 , side3 = eval(input("Enter three sides in double : "))
    
    if isValid(side1, side2, side3) == True :
        area(side1, side2, side3)

    else :
        print()
        print("Input is invalid")

main()
        
    
