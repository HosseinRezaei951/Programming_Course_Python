from random import randint

def getRandomUpperCaseLetter(ch1,ch2):
    count = 1
    occurrence = 0 
    while count <= 10000 :
        CHR = chr(randint(ord(ch1),ord(ch2)))
        print(CHR,end=" ")
        if CHR == 'A' :
            occurrence += 1
            
        if count % 10 == 0 :
            print()

        count += 1 

    print()
    print("The occurrence of A is ",occurrence)

def main():
    getRandomUpperCaseLetter('A','Z')

main()
        
        
        
        
