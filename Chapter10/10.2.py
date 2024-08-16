List = input("Plz enter numbers : ")
lst = []
item = List.split()
lst = [x for x in item]

n = len(lst)
for i in range(n-1 , -1 , -1 ) :
    print(lst[i],end=" ")
