def eliminateDuplicates(lst):
    lst2 = []
    n = len(lst)
    
    for i in range(0,n):
        flag = True
        for j in range(0,i):
            if lst[i] == lst[j] :
                flag = False

        if flag == True :
            lst2.append(lst[i])
    
            

  
    print("The distinct numbers are : ",end="")
    for i in range(0,len(lst2)):
        print(lst2[i],end=" ")
        

def main():
    lst = []
    numbers = input("Enter ten numbers: ")
    List = numbers.split()
    lst = [eval(x) for x in List]
    
    eliminateDuplicates(lst)
    
    
main()    
