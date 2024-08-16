def stringer(lst):
    a = ""
    for i in range(len(lst)):
        a = a + str(lst[i])

    return a

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

def mul(num1,num2):
        
    
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
    return first
            
            

def minus(num1):
    
    num2 = "1"
    L1 = len(num1)
    L2 = len(num2)

    big1 = []
    small1 = []
    if L1 > L2 :
        for i in range(0,L1):
            big1.append(num1[i])
        for j in range(0,L2):
            small1.append(num2[j])
    elif L1==L2:
        a=eval(num1)
        b=eval(num2)
        if a>=b:
            for i in range(0,L1):
               big1.append(num1[i])
            for j in range(0,L2):
               small1.append(num2[j])         
        else:
            for i in range(0,L2):
               big1.append(num2[i])
            for j in range(0,L1):
               small1.append(num1[j])
              
               

    else :
        for i in range(0,L2):
           big1.append(num2[i])
        for j in range(0,L1):
          small1.append(num1[j])
          
    s=len(big1)-len(small1)
    for w in range(s):
        small1.insert(0,str(0))
        

    big=[]
    for l in range(len(big1)):
        big.append(eval(big1[l]))
        
    small=[]
    for e in range(len(small1)):
        small.append(eval(small1[e]))    
    for x in range(1,len(big)):
                A=big[-x]
                B=small[-x]
                if A<B :
                    big[-x]=big[-x]+10
                    big[-x-1]=big[-x-1]-1     

    j=[]  
    for k in range(1,len(big)+1):      
                 A=(big[-k])-(small[-k])
                 j.insert(0,abs(A))

    return j

def fac(n):
    
    R = ["1"]
    N = [ x for x in n ]
    
    
    while N != ["-1"] :
        
        R = [ x for x in (mul(stringer(N),stringer(R))) ]
        N = [ x for x in (minus(stringer(N))) ]
        
        
        flag = True
        for i in range (0,len(N)):
            if N[i] != 0 :
                flag = False

        if flag == True :
            return R     

def main():
    num = input("Plz enter a number : ")
    n = []
    if num == "0" or num == "1" :
        print("1")

    else :
        
        for i in range(0,len(num)):
            n.append(num[i])
        ANSWER = [ x for x in fac(n) ]
        for i in range(0,len(fac(n))):
            if ANSWER[0] == 0 :
                ANSWER.pop(0)
                    
        for i in range(0,len(ANSWER)):
            print(ANSWER[i],end="")

main()

    

    
