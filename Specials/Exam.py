n = eval(input("enter a number:"))
N = 1
for i in range(1,n+1,+2):
    N = 1
    for j in range(i,0,-1):
        A = j*((-1)**N)
        print(A,end=" ")
        N += 1 

    print()
    

