def Sum(num1,num2):
    
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
        Sum = (big[L_big-1]) + (small[L_small-1])
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
        Sum = (big[L_big-1])
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
    ans = []
    for i in range(len(lst_sum)-1,-1,-1):
        ans.append(lst_sum[i])

    return ans

def main():
    num1 = input("Enter a number1 : ")
    num2 = input("Enter a number2 : ")
    
    print()
    print(num1+"*"+num2,"=")
    L1 = len(num1)
    L2 = len(num2)

    up = []
    down = []
    if L1 >= L2 :
        for i in range(0,L1):
            up.append(num1[i])
        for j in range(0,L2):
            down.append(num2[j])

    else :
        for i in range(0,L2):
            up.append(num2[i])
        for j in range(0,L1):
            down.append(num1[j])

    
    L1 = len(up)
    L2 = len(down)
    
    for i in range(L2-1,-1,-1):
        D = 0
        ans = []
        for j in range(L1-1,-1,-1):
            mul = eval(down[i])*eval(up[j])

            if D+mul < 10 :
                ans.insert(0,(mul+D))
                D = 0

            elif D+mul >= 10 :
                ans.insert(0,((mul+D)%10))
                D = (D+mul)//10
                
        if D != 0 :
            ans.insert(0,D)
            
        for z in range(1,L2-i):
            ans.append(0)


            
        if i == L2-1 :
            first = [ x for x in ans]
            

        else :           
            first = [ x for x in (Sum(first,ans))]
    for x in first :
        print(x,end="")
            
            
main()
                
                

    


    




    
