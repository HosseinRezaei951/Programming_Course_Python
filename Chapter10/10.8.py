def Min(lst):
    Min = 99999999999999999999999999999
    for i in range(0,len(lst)):
        if lst[i] <= Min :
            Min = lst[i]

    return Min


def indexOfSmallestElement(Min,lst):
    for i in range(0,len(lst)):
        if lst[i] == Min :
            Index = i
            break

    return Index
        

def main():
    lst = []
    number = input("Enter number : ")
    List = number.split()
    lst = [eval(x) for x in List]
    
    print("The smallest element is",Min(lst),"and the index is",indexOfSmallestElement(Min(lst),lst))
    
    
    
main()    



        
        
