def count(s):
    L = len(s)
    lst = []
    for i in range(0,L):
        lst.append(s[i])
        
    L2 = len(lst)
    for i in range(0,L2):
        for j in range(i+1,L2):
            if lst[i] > lst[j] :
                lst[i] , lst[j] = lst[j] , lst[i]
    
    count = 0
   
    
    for i in range(0,L2):
        count = 0
        for j in range(0,L2):
                        
            if lst[i] == lst[j] :
                count += 1
                
        print(lst[i]," occurs ",count," times")



def main():
    
    s = input("Enter a string : ")
    count(s)
    
    
main()   
