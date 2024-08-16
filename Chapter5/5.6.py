one_Miles_per_kilometers = 1.609
one_kilometers_per_Miles = 0.621
count = 1
count2 = 20
print("Miles \t     kilometers   |  kilometers \t Miles")

for count in range ( 1 , 66 ):
            
            K = one_Miles_per_kilometers * count


            if count < 66 :
                        M = one_kilometers_per_Miles * count2

            if count < 7 :

                        print (count,"\t","   ",format(K,".3f"),"       | ",count2,"        \t",format(M,".3f"))

            if 6 < count < 11 :

                        print (count,"\t","   ",format(K,".3f"),"      | ",count2,"         \t",format(M,".3f"))
            
            
            if count > 11 and count2 < 66:
                        
                       print ("\t""\t""\t""  | ",count2,"         \t",format(M,".3f")) 
             
            count += 1
            count2 += 5

            
                        
            
           

            
