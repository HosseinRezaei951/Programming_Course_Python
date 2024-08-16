import random

lst = []
for i in range(0,1000):
   num = random.randint(0,9)
   lst.append(num)

lst2 = []
for i in range(0,10):
    count = 0
    for j in range(0,1000):
            if lst[j] == i :
                count += 1

    lst2.append(count)

for i in range(0,10):
    print(lst2[i],"times",i)
    
                            
