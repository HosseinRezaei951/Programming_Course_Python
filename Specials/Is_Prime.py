def emirp(num):

    count = 0
    number = 1
    
    while count <= num-1 :
        
        
        
            divisor = 2
            flag = False
            while divisor <= (number / 2)+1 and flag == False :
                
                if number % divisor == 0:
                    flag =  False 
                divisor += 1
            if flag == False :
                print(format(number,"<4d"),end=" ")
                count += 1 
                number += 1
                if count % 10 == 0 :
                    print()
                

            
                
         
        

def main():
    num = eval(input("Plz enter a number : "))
    emirp(num)
    
    

main()
    
    
