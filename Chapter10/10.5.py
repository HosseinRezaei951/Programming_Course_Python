def Sort(lst):
    n = len(lst)
    for i in range(n-1):
        for j in range(i+1,n):
            if lst[i] > lst[j]:
                lst[i],lst[j] = lst[j],lst[i]

    
    return lst



def DistinctNumbers(lst):
    lst2 = [0]
    for i in range(0,len(lst)):
        flag = True
        for j in range(len(lst2)):
            if lst[i] == lst2[j] :
                flag = False

            else :
                flag = True

        if flag == True :
            lst2.append(lst[i])
            
                
    print("The distinct numbers are: ",end="")
    for i in range(1,len(lst2)):
        print(lst2[i],end=" ")
    




def main():
    lst = []
    score = input("Enter scores : ")
    List = score.split()
    lst = [eval(x) for x in List]
    
    DistinctNumbers(Sort(lst))
    
    
main()    



        
        
