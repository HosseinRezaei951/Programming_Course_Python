def m(i) :
    
    print("i\t\t m(i)")
    print()
    s = 0
    for n in range(1,i+1,100):
        s = 0
        for x in range(1,n+1):
            
            y = ((-1)**(x+1))/((2*x)-1)
            s = s + y
          
        print(n,"\t\t",format(4*s,"1.4f"))

def main() :
    i = 901
    m(i)

main()
        
