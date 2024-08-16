number=eval(input("Enter a number between 0 and 1000:"))

tens=number//100

hundreds=(number%100)//10

thousands=(number%100)%10

digits=tens+hundreds+thousands

print("The sum of the digits is",digits)
