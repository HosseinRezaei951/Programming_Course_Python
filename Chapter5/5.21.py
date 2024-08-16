i = 1
count = 0
dash = " "

while count != 8 :
    print((30-4*count)*dash,end=" ")
    
    for i in range( -count , count+1 ):
        
        print(format((2**(count-abs(i))),"4.0f"),end="")
        
    count += 1
    print()
  
    
print()
                
