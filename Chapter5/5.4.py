count = 0
Miles = 1
one_Miles_per_kilometers = 1.609

print("Miles","\t","kilometers")

while count < 10 :
            kilometers = Miles * one_Miles_per_kilometers
            
            print (Miles,"\t",format(kilometers,".3f"))
            
            Miles += 1
            count += 1
