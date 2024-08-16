print ("numbers divisible by 5 and 6 are : ")
count = 1
for number in range ( 99 , 1000) :
             
            if (( number % 5 )==0) and (( number % 6 )==0):

                        print (str(number),end=" ")
                        
                        if (count % 10) == 0 :
                                    print("\n")

                        count += 1
                        
