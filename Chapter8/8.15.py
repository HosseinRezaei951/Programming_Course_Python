num = input("Enter the first 9 digits of an ISBN-10 as a string: ")

s = 0
i = 1
j = 0 
while i <= 9:
    s = s + ( i *( eval(num[j])))
    i += 1
    j += 1


D10 = s % 11
X = 'X'

if D10 == 10 :
    print("The ISBN-10 number is "+num+str(X))

else :
    print("The ISBN-10 number is "+num+str(D10))


    

