def pentagonal_number(n):
    num = (n*((3*n)-1))/2
    return int(num)

def main():
    n = eval(input("Plz enter a number : "))
    print("The first",n," pentagonal numbers : ")
    count = 0
    for n in range(1,n+1):
        A = pentagonal_number(n)
        print(format(A,"<6.0f"),end=" ")
        count += 1
        
        if count % 10 == 0 :
            print()

        

main()
        
        
