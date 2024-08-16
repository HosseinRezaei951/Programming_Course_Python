def isConsecutiveFour(lst):
    count = 0
    for i in range(0,len(lst)):

        if i < (len(lst)-4) :
            for j in range(i,i+2):
                if lst[i] == lst[j]:
                    count += 1
                    
        elif i == (len(lst)-4) :
            for j in range(i,i+2):
                if lst[i] == lst[j]:
                    count += 1

        elif i > (len(lst)-4) :
            break

    if count == 4:
        print("list contains four consecutive numbers with the same value.")

    elif count > 5:
        print("list contains mor than four consecutive numbers with the same value.")
        
    elif count < 4:
        print("list not contains four consecutive numbers with the same value.")      

def main():
    lst = []
    List = input("Plz Enter a series of integers : ")
    List = List.split()
    lst = [eval(x) for x in List]
    
    isConsecutiveFour(lst)
    
    
main()   
