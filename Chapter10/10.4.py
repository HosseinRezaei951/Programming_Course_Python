def Average(lst):
    Sum = 0
    for i in range(0,len(lst)):
        Sum += lst[i]
    Average = Sum / len(lst)
    
    return Average


def AnalyzeScores(lst,Average):
    above_or_equal = 0
    below = 0
    for i in range(0,len(lst)):
        
        if lst[i] >= Average :
            above_or_equal += 1
        
        else :
            below += 1

        
    print(above_or_equal,"scores are above or equal to the average")
    print(below,"scores are below the average")

def main():
    lst = []
    score = input("Enter scores : ")
    List = score.split()
    lst = [eval(x) for x in List]
    
    AnalyzeScores(lst,Average(lst))
    
    
main()    



        
        
