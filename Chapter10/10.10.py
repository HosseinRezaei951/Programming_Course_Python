def reverse(lst):
    n = len(lst)
       
    if n % 2 == 0 :
        j = n-1 
        for i in range(0,round(n/2)):
            
            lst[i] , lst[j] =  lst[j] ,  lst[i]
            j -= 1
        for i in range(0 , n):
            print(lst[i],end=" ")

    else :
        j = n-1 
        for i in range(0,(round(n/2))-1):
            
            lst[i] , lst[j] =  lst[j] ,  lst[i]
            j -= 1
        for i in range(0 , n):
            print(lst[i],end=" ")
        

        
        
       
    
def main():
    lst = []
    item = input("Enter list : ")
    List = item.split()
    lst = [eval(x) for x in List]
    reverse(lst)
 
main()    



        
        
