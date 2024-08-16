num1 = input("Enter a number1 : ")
num2 = input("Enter a number2 : ")

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

print()
print("|"+num1+"-"+num2+"|","=")
for i in range(0,len(j)):
    print(j[i],end="")
    

    


    


