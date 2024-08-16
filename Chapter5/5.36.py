import random

PC_WIN = 0
USER_WIN = 0

while PC_WIN <= 3 or USER_WIN <= 3 :

            if USER_WIN == 3 :
                print("\n Finally you won the game.")
                break

            elif PC_WIN == 3 :
                print("\n Sorry ,Finally you lose.")
                break

        
            rand = random.randint(0,2)
            guess = eval(input("\nscissor (0), rock (1), paper (2): "))

            if ( (rand == guess) and (rand == 0) ) :
                        print("\t The computer is scissor. You are scissor too. It is a draw.")
                                    
                        

            elif ( (rand == guess) and (rand == 1) ) :
                        print("\t The computer is rock. You are rock too. It is a draw.")
                        
                        

            elif ( (rand == guess) and (rand == 2) ) :
                        print("\t The computer is paper. You are paper too. It is a draw.")
                        
                        
                        


            #scissor VS rock
            elif ( (rand == 0) and (guess == 1) ) :
                        print("\t The computer is scissor. You are rock. You won.")
                       
                        
                        


            elif ( (rand == 1) and (guess == 0) ) :
                        print("\t The computer is rock. You are scissor. You lose.")
                        PC_WIN += 1
                        


            #scissor VS paper
            elif ( (rand == 0) and (guess == 2) ) :
                        print("\t The computer is scissor. You are paper. You lose.")
                        PC_WIN += 1
                        


            elif ( (rand == 2) and (guess == 0) ) :
                        print("\t The computer is paper. You are scissor. You won.")
                        USER_WIN += 1
                        


            #rock VS paper
            elif ( (rand == 1) and (guess == 2) ) :
                        print("\t The computer is rock. You are paper. You won.")
                        USER_WIN += 1
                        


            elif ( (rand == 2) and (guess == 1) ) :
                        print("\t The computer is paper. You are rock. You lose.")

                        PC_WIN += 1


            
    
    


                


            
