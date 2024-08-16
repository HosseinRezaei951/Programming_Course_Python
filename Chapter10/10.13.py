def sort(lst):
    n = len(lst)
    for i in range(n-1):
        for j in range(i+1,n):
            if lst[i] > lst[j] :
               lst[i] , lst[j] = lst[j] , lst[i]
    
    return lst

def eliminateDuplicates(lst):
    lst2 = []
    n = len(lst)
    
    for i in range(0,n+1):
            k = i + 1
            flag = False
            
            if i == (n-1) and lst[i] != lst[i-1] :
                lst2.append(lst[i])
                break
            
            elif i == (n-1) and lst[i] == lst[i-1]:
                break
            
            if lst[i] == lst[k] :
                flag = True
                
            if flag == False :
                lst2.append(lst[i])

  
    print("The distinct numbers are : ",end="")
    for i in range(0,len(lst2)):
        print(lst2[i],end=" ")
        

def main():
    lst = []
    numbers = input("Enter ten numbers: ")
    List = numbers.split()
    lst = [eval(x) for x in List]
    
    eliminateDuplicates(sort(lst))
    
    
main()    
