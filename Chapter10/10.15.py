def isSorted(lst):
    n = len(lst)
    flag = False
    k = 0 
    for i in range(1,n):
        if lst[i] >= lst[k] :
            flag = True
            k = i

        else :
            flag = False


    if flag == True :
        print("The list is already sorted")
        
    elif flag == False :
        print("The list is not sorted")
  
def main():
    lst = []
    item = input("Enter a score : ")
    List = item.split()
    lst = [eval(x) for x in List]
    
    isSorted(lst)
    
    
main()    

