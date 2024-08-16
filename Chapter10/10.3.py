def occurs(lst):
    occurs = 0
    num = 999999999999
    for i in range(0,len(lst)):
        counter = 0
        
        if lst[i] != num :
            
            for j in range(0,len(lst)):
                if lst[i] == lst[j] :
                    counter += 1
                    num = lst[i]
                else :
                    num = lst[i]
                    
                   
            print(lst[i],"occurs",counter,"times")

                 

def main():
    lst = []
    score = input("Enter integers between 1 and 100 : ")
    List = score.split()
    lst = [eval(x) for x in List]
    lst.sort()
    occurs(lst)
        
main()    



        
        
