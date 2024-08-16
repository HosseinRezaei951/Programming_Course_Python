def sqrt(n):
    x = n
    y = 1
    e = 0.0000000000000000000000000000001
    while x - y > e :
        x = (x+y)/2
        y = n/x

    else :
        return x
        
        
        

def main():
    num = eval(input("Plz enter a number : "))
    print("The approximate the square root of "+str(num),"is : ",sqrt(num))

main()
