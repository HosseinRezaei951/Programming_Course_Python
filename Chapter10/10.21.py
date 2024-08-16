lst = 100 * [False]

#s1 :
for i in range(0,len(lst)):
    lst[i] = True
#s2 :
for i in range(2,len(lst)):
    lst[i] = False

for j in range(3,101):
    for i in range(j-1,len(lst),j):
        if lst[i] == False :
            lst[i] = True
        else :
            lst[i] = False
count = 0
for i in range(0,len(lst)):
    if lst[i] == True :
        count += 1


     
print("After all the students have passed through the building and changed the lockers",count,"lockers are open.")

