def Max(lst):
    Max = 0
    for i in range(0,len(lst)):
        if lst[i] >= Max :
            Max = lst[i]

    return Max

def gcd(lst,Max):
    flag = False
    while flag == False :
        
        for i in range(0,len(lst)):
            flag = True
            if lst[i] % Max == 0 :
                if i == ((len(lst))-1) :
                    print("The GCD of these numbers is :",Max)

            else :
                Max -= 1
                flag = False
                break
                

def main():
    lst = []
    List = input("Enter List : ")
    List = List.split()
    lst = [eval(x) for x in List]
    
    gcd(lst,Max(lst))
    
    
    
main()    
