lst = []
item = input("Plz enter 10 integers : ")
List = item.split()
lst = [eval(x) for x in List]

n = len(lst)
print()
for i in range(0,n):
    count = 0
    for j in range(0,n):
        print(lst[i],"+",lst[j],"=",(lst[i]+lst[j]),"\t",end="")
        count += 1
        if count == 10 :
            print("\n")
