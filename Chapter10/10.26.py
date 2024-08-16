def merge(lst1, lst2):
    L = len(lst1) + len(lst2)
    List = []
    List = lst1 + lst2
    
    for i in range(0,L):
        for j in range(i+1,L):
            if List[i] > List[j] :
                List[i] , List[j] = List[j] , List[i]

    print("The merged list is ",end="")
    for x in List :
        print(x,end=" ")
            
def main():
    lst1 = []
    list1 = input("Enter list1 : ")
    List1 = list1.split()
    lst1 = [eval(x) for x in List1]

    lst2 = []
    list2 = input("Enter list2 : ")
    List2 = list2.split()
    lst2 = [eval(x) for x in List2]
    
    
    merge(lst1, lst2)
    
    
main()    
