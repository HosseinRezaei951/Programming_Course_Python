import random

rand = random.randint(0,2)

guess = eval(input("scissor (0), rock (1), paper (2): "))

if ( (rand == guess) and (rand == 0) ) :
            print("The computer is scissor. You are scissor too. It is a draw.")

elif ( (rand == guess) and (rand == 1) ) :
            print("The computer is rock. You are rock too. It is a draw.")

elif ( (rand == guess) and (rand == 2) ) :
            print("The computer is paper. You are paper too. It is a draw.")


#scissor VS rock
elif ( (rand == 0) and (guess == 1) ) :
            print("The computer is scissor. You are rock. You won.")


elif ( (rand == 1) and (guess == 0) ) :
            print("The computer is rock. You are scissor. You lose.")


#scissor VS paper
elif ( (rand == 0) and (guess == 2) ) :
            print("The computer is scissor. You are paper. You lose.")


elif ( (rand == 2) and (guess == 0) ) :
            print("The computer is paper. You are scissor. You won.")


#rock VS paper
elif ( (rand == 1) and (guess == 2) ) :
            print("The computer is rock. You are paper. You won.")


elif ( (rand == 2) and (guess == 1) ) :
            print("The computer is paper. You are rock. You lose.")


            
