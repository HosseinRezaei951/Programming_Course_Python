import random

count = 0

for i in range (0,1000000):
    
    X = random.randint(-10,+11)
    Y = random.randint(-10,+11)

    if (X < 0 and Y < 0) or (X < 0 and Y > 0) or (X > 0 and Y > 0 and Y<= 10-X):
        count += 1

print("what is the probability for the dart to fall into an odd-numbered region : "\
      ,count)
      
        
        

