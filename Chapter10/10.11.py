def shuffle(lst):
    import random
    for i in range(0,len(lst)):
        rand1 = random.randint(0,(len(lst)-1))
        rand2 = random.randint(0,(len(lst)-1))
        lst[rand1] , lst[rand2] =  lst[rand2] , lst[rand1]
        

    for i in range(0,len(lst)):
        print(lst[i],end=" ")
        
def main():
    lst = []
    number = input("Enter number : ")
    List = number.split()
    lst = [eval(x) for x in List]
    
    shuffle(lst)
    
    
main()    
