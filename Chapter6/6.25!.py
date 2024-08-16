def emirp(num):

    if num // 1000 == 0 :
        
        digit1 = num % 10
        r1 = num // 10

        digit2 = r1 % 10
        digit 3 = r2 // 10

        num = (digit3)+(digit2*10)+(digit1*100)

    elif num // 100 == 0 :
        digit1 = num % 10
        digit2 = num // 10
        num = (digit2)+(digit1*10)


    flag =  False
    i = 2

    while i <= (m**0.5) and flag == False :
        r = m % i
        if r == 0 :
            flag = True

        if flag == False :
        return True

        i += 1

    
            
        

    

    
        
        
        







def prime(num):

    m = 2
    count = 0
    while count < num :
        flag =  False
        i = 2

        while i <= (m**0.5) and flag == False :
            r = m % i
            if r == 0 :
                flag = True

            i += 1

        if flag == False :
            count += 1
            
            print(format(m,"<5d"),end=" ")
            if count % 10 == 0 :
                print()

        m += 1

        

        

def main():

    num = eval(input("Plz enter a number : "))
    prime(num)

main()
