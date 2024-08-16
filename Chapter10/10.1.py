def BestScore(lst):
    Max = 0
    for i in range(0,len(lst)):
        if lst[i] >= Max :
            Max = lst[i]

    return Max


def WhatGrad(lst,Max):
    for i in range(0,len(lst)):
        
        if lst[i] >= (Max-10) :
            grade = "A"
            
        elif lst[i] >= (Max-20) :
            grade = "B"

        elif lst[i] >= (Max-30) :
            grade = "C"

        elif lst[i] >= (Max-40) :
            grade = "D"

        else :
            grade = "F"

        print("Student",i,"score is",lst[i],"and grade is",grade)

def main():
    lst = []
    score = input("Enter a score : ")
    List = score.split()
    lst = [eval(x) for x in List]
    
    WhatGrad(lst,BestScore(lst))
    
    
main()    



        
        
