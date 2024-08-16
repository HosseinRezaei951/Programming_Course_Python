import random

rand1 = random.randint(1,4)
rand2 = random.randint(1,13)

#suit
if rand1 == 1 :
            suit = 'Clubs'
elif rand1 == 2 :
            suit = 'Diamonds'
elif rand1 == 3 :
            suit = 'Hearts'
elif rand1 == 4 :
            suit = 'Spades'

#rank
if rand2 == 1 :
            rank = 'Ace'
elif rand2 == 2 :
            rank = '2'
elif rand2 == 3 :
            rank = '3'
elif rand2 == 4 :
            rank = '4'
elif rand2 == 5 :
            rank = '5'
elif rand2 == 6 :
            rank = '6'
elif rand2 == 7 :
            rank = '7'
elif rand2 == 8 :
            rank = '8'
elif rand2 == 9 :
            rank = '9'
elif rand2 == 10 :
            rank = '10'
elif rand2 == 11 :
            rank = 'Jack'
elif rand2 == 12 :
            rank = 'Queen'
elif rand2 == 13 :
            rank = 'King'

print("The card you picked is the",rank,"of",suit)


      
            

            



