import random

head = 0
tail = 0

for i in range(0,1000000):
    TRY = random.randint(0,1)

    if TRY == 0 :
        head += 1

    else :
        tail += 1

print("After 1 million times flipping a coin : "\
      ,head," is head and ",tail," is tail")
