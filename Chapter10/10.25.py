import random
count = 0
times = 0

for a in range(1,14):
    for b in range(1,14):
        for c in range(1,14):
            for d in range(1,14):
                print(a,b,c,d)
                count += 1
                if (a+b+c+d) == 24 :
                    print("\t","\t",a,"+",b,"+",c,"+",d,"=",a+b+c+d)
                    times += 1

                    

print("After ",count," times shuffling ",times," times,The sum of the numbers on the cards was 24.")


        

