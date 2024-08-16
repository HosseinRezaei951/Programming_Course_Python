integer=eval(input("Enter an integer:"))

A=integer//1000
R1=integer%1000

B=R1//100
R2=R1%100

C=R2//10
R3=R2%10

D=R3//1
R4=R3%1

print("The reversed number is",str(D)+str(C)+str(B)+str(A))
