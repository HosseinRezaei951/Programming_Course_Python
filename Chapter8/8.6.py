def countLetters(s):
    count = 0
    i = 0
    x = len(s)
    while i <= x :
        R = s[i]
        if i == x :
            return count
        
        elif not(R.isalpha() == True):
            i += 1
        
            
        elif R.isalpha() == True:
                    count +=1
                    i += 1
                    if i == x and count != 0:
                        return count
                        break
       
                    
        

    if count == 0 : 
            print("The number of letters in the string : 0")
            

        
        
    
            

def main():
    string = (input("Plz enter a string : ")).strip()
    
    print("The number of letters in the string : ",countLetters(string))
    

main()
