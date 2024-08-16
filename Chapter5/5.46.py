import math

print("Enter ten numbers: ",end="")

sigma1 = 0
sigma2 = 0

for n in range( 1 , 11 ) :
    num = eval(input())
    sigma1 = sigma1 + num
    sigma2 = sigma2 + (num**2)

mean = sigma1 / 10

deviation = math.sqrt((sigma2 - ((sigma1**2)/10)) / 9 )

print("The mean is ",format(mean,".2f"))
print("The standard deviation is ",format(deviation,".5f"))




