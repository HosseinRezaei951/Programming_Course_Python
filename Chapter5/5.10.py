number = eval(input("Plz enter the number of students: "))
count = 1 
high_score = 0
while count < (number+1) :
    score = eval(input("Plz enter the student "+str(count)+" score: "))

    if score > high_score :
        high_score = score
        
    count += 1 
            
print("The highest score is ", high_score)

            
            
 
