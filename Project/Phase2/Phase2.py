#sum
def Revers(lst):
        Length = len(lst)
        revers = []
        for i in range(Length-1,-1,-1):
                revers.append(lst[i])

        return revers
                
def Printer(lst):
        Length = len(lst)
        for i in range(0,Length):
            print(lst[i],end="")
        
        
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


        return lst_sum 


#minus
def Minus(num1,num2):
    
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
                
            

#mult
def Mult(num1,num2):

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
                

def main():
    num1 = input("Enter a number1 : ")
    num2 = input("Enter a number2 : ")
    print()
    
    #Sum    
    print(num1+"+"+num2,"=")
    Printer(Revers(Sum(num1,num2)))
    print("\n\n")

    #Minus
    print("|"+num1+"-"+num2+"|","=")
    Printer(Minus(num1,num2))
    print("\n\n")

    #Mult
    print(num1+"*"+num2,"=")
    Mult(num1,num2)
    print("\n\n")
     
    
main()
                
                

    


    




    

    



