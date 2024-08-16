def mean(lst):
    mean = sum(lst)/len(lst)

    return mean
    
def deviation(lst,mean):
    import math
    lst2 = []
    for i in range(0,len(lst)):
        f = (lst[i] - mean)**2
        lst2.append(f)
        
    deviation = math.sqrt( (sum(lst2)) / (len(lst2)-1) )

    return deviation

def main():
    lst = []
    score = input("Enter a score : ")
    List = score.split()
    lst = [eval(x) for x in List]
    
    print("The mean is",format(mean(lst),".2f"))
    print("The standard deviation is",format(deviation(lst,mean(lst)),".5f"))
    
    

main()

