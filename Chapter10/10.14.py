def selectionSort(lst):
    n = len(lst)
    Max = 0
    for i in range(0,n):
        if lst[i] >= Max :
            Max = lst[i]

    L = lst.index(Max)
    lst[L] , lst[n-1] = lst[n-1] , lst[L]

    for i in range(n-1,-1,-1):
        for j in range(i-1,-1,-1):
            if lst[i] < lst[j] :
                lst[i] , lst[j] = lst[j] , lst[i]
    
    for x in lst :
        print(x,end=" ")
        
def main():
    lst = []
    number = input("Enter ten numbers: ")
    List = number.split()
    lst = [eval(x) for x in List]
    
    selectionSort(lst)
    
    
main()    
