import random

rand = random.randint(0,1)

guess = eval(input("Enter a guess ( Ex : 0 for head or 1 for tail ): "))

if ( (rand == guess) and (guess == 0) )  :
            print("Congratulations ... the guess is correct."\
                  " coin is head")

elif ( (rand == guess) and (guess == 1) )  :
            print("Congratulations ... the guess is correct."\
                  " coin is tail")

elif ((rand != guess) and (guess == 0))  :
            print("Oops ... the guess is incorrect."\
                  " coin is head")

elif ((rand != guess) and (guess == 1))  :
            print("Oops ... the guess is incorrect."\
                  " coin is tail")

