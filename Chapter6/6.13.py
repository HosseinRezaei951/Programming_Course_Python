  def m(i):
    
    print("i\t\t m(i)")
    print()
    s = 0
    for n in range(1,i+1):
        s = 0
        for x in range(1,n+1):
            
            y = (x/(x+1))
            s = s + y
          
        print(n,"\t\t",format(s,"2.4f"))

def main() :
    i = 20
    m(i)

main()
