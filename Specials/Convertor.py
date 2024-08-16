def emirp( n ) :
    x = 10
    i = 1
    r = 1
    ALL = 0
    digit = 0
    digit2 = 1
    digit3 = 2
    
        
    while n % (x**i) <= n and digit2 > 0 and digit3 > 1:
        part = ( n % (x**i) )
        
        if n % (x**i) == n :
            digit3 = n // (x**(i-1))
            print(digit3,end="")
        elif part < 10 :
            digit1 = part
            print(digit1,end="")  
        else :
            digit2 = part // (x**(i-1))    
            ALL = ALL + digit2
            print(digit2,end="")
            
        i += 1
        
      
    

def main() :
    num = eval(input("Plz enter a number : "))
    emirp(num)

main()
    
