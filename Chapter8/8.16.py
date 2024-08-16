num = input("Enter the first 12 digits of an ISBN-13 as a string: ")

s = 0
i = 1
j = 0 
while i <= 12:
    if i % 2 == 0 :
        s = s + (3*( eval(num[j])))

    else :
        
        s = s + ( eval(num[j]))
    i += 1
    j += 1


D10 = (10-s) % 10
X = '0'

if D10 == 10 :
    print("The ISBN-13 number is "+num+str(X))

else :
    print("The ISBN-13 number is "+num+str(D10))


    

