num1 = input("Enter a number1 : ")
num2 = input("Enter a number2 : ")

L1 = len(num1)
L2 = len(num2)

big = []
small = []
if L1 >= L2 :
    for i in range(0,L1):
        big.append(num1[i])
    for j in range(0,L2):
        small.append(num2[j])

else :
    for i in range(0,L2):
        big.append(num2[i])
    for j in range(0,L1):
        small.append(num1[j])

L_big = len(big)
L_small = len(small)

lst_sum = []
R = 0
while L_small > 0 :
    Sum = eval(big[L_big-1]) + eval(small[L_small-1])
    L_big -= 1
    L_small -= 1
    
    if (Sum+R) >= 10 :
        lst_sum.append((Sum+R)%10)
        R = (Sum+R) // 10
        
    else :
        lst_sum.append((Sum+R)%10)
        if ((Sum+R)) < 10 :
            R = 0
        
while (L_small <= 0 and L_big > 0) :
    Sum = eval(big[L_big-1])
    L_big -= 1
    if (Sum+R) >= 10 :
        lst_sum.append((Sum+R)%10)
        R = (Sum+R) // 10
        
     
    else :
        lst_sum.append((Sum+R)%10)
        if ((Sum+R)) < 10 :
            R = 0
        
if R != 0 :
    lst_sum.append(R)

print()
print(num1+"+"+num2,"=")

L_lst_sum = len(lst_sum)
for i in range(L_lst_sum-1,-1,-1):
    print(lst_sum[i],end="")


    


