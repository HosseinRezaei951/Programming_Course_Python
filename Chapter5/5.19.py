import sys


n = eval(input("Enter the number of lines ( 1 to 15 ): "))
if not(1 <= n <= 15):
    sys.exit()
    
i = 1
count = n
R = ""
dash = " "

while count != 0 :
    print(str(R)+(3*count)*dash,end="")
    
    for i in range( n-count , (-n+count)-1 , -1):
        print(format(abs(i)+1,"2.0f"),end=" ")
        
    count -= 1
    print()
  
    
print()
                
