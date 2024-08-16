import sys

def isbig(num1,num2):

    L1 = len(num1)
    L2 = len(num2)

    
    flag = True
    
    if L1==L2:
        for i in range(0,L1):
            if num1[i] > num2[i] :
                flag = True
                break

            elif num1[i] < num2[i] :
                flag = False
                break        
           
    elif L1 > L2 :
        flag = True
    elif L2 > L1 :
        flag = False
    
    return flag
    
        
def POP(ANSWER):
    for i in range(0,len(ANSWER)):
            if ANSWER[0] == 0 :
                ANSWER.pop(0)
    
    return ANSWER

    
def STR(lst):
    ANS = [ str(x) for x in lst ]
    return ANS

def EVAL(lst):
    ans = [ eval(x) for x in lst]
    return ans

def STRING(lst):
    a = ""
    for i in range(0,len(lst)):
        a = a + str(lst[i])

    return a

def Minus(num1,num2):
    
    L1 = len(num1)
    L2 = len(num2)

    big1 = []
    small1 = []
    
    for i in range(0,L1):
            big1.append(num1[i])
    for j in range(0,L2):
            small1.append(num2[j])
    
          
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

        
def divi():
    
    num1 = input("Enter a number1 : ")
    num2 = input("Enter a number2 : ")

    L1 = len(num1)
    L2 = len(num2)
    big = []
    small = []
    if L1 > L2 :
        for i in range(0,L1):
            big.append(num1[i])
        for j in range(0,L2):
            small.append(num2[j])
    elif L1==L2:
        a=eval(num1)
        b=eval(num2)
        if b >= a :
            print("0")
            sys.exit()
              
        else :
            for i in range(0,L1):
               big.append(num1[i])
            for j in range(0,L2):
               small.append(num2[j])                 

    else :
        print("0")
        sys.exit()
   
    s=len(big)-len(small)
    for w in range(s):
        small.insert(0,str(0))
    
    count = 0
    S = STRING(small)
    
        
    while isbig(EVAL(big),EVAL(small)) == True :
        big = [ x for x in STR(Minus(STRING(big),S))]
        count += 1
    
    if POP(EVAL(big)) == [] :
           print("0")
    for i in range(0,len(POP(EVAL(big)))):
        print(POP(EVAL(big))[i],end="")
    
        
    

divi()



