j = 0
B = 1
A = 1
for i in range(10000,100000,10000):
    A = 1
    B = 1
    j = 0 
    while A <= i :

        B = A * B
        j = (1/B) + j
        A += 1

    print("sum the following series : \n"\
          " \t 1+ 1/1! + 1/2! + ... + 1/"+str(i)+"! = "+str(1+j))

