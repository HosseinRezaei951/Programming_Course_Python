def sumDigits(n):
    x = 10
    i = 1
    r = 1
    ALL = 0
    digit = 0
    
    while n % (x**i) != n :
        part = ( n % (x**i) )
        
        if part < 10 :
            digit1 = part
           
        else :
            digit2 = part // (x**(i-1))    
            ALL = ALL + digit2
            
            
        i += 1
        
    if n % (x**i) == n :
        digit3 = n // (x**(i-1)) 
      

    print(digit1+digit3+ALL)

def main():
    num = eval(input("Plz enter a number : "))
    sumDigits(num)

main()
        
        
        
        
