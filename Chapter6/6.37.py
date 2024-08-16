from random import randint
import turtle
def getRandomUpperCaseLetter(ch1,ch2):
    count = 1
    turtle.penup()
    turtle.goto(-100,100)
    i = 1
    while count <= 100 :
        turtle.pendown()
        CHR = chr(randint(ord(ch1),ord(ch2)))
        turtle.write(CHR,font=(16))
        turtle.penup()
        turtle.forward(20)
        
        
        
        if count % 10 == 0 :
            turtle.penup()
            turtle.goto(-100,100-(20*i))
            i += 1

        count += 1 

    
def main():
    getRandomUpperCaseLetter('A','Z')

main()
        
        
        
        
