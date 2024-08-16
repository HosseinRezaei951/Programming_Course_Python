num = eval(input("Plz enter a number : "))
i = 0 
while num // (10**i) >= 0 :
    if num // (10**i) == 0 :
        print(i)
        break
    i += 1 
