def fac(n):
    R = 1
    for i in range(1,n+1):
        n = []
        
        R = (R * n)
        print(R)
        n -= 1
        if n == 1 :
            return R

def main():
    num = input("Plz enter a number : ")
    n = []
    for i in range(0,len(num)):
        n.append(num[i])

    print(n)
    #print(str(num)+"! = ",fac(num))

main()

    

    
