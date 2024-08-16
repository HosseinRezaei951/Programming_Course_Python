print("All the prime numbers between 2 and 1,000 : ")
count = 1
n = 1000
m = 2
while m < n :
    flag = False
    i = 2

    while i <= (m**0.5) and flag == False :
        r = m % i
        if r == 0 :
            flag = True

        i = i+1

    if flag == False :
        print(m,end=" ")
        if count % 8 == 0 :
            print("\n")
    
    
        count += 1

    m += 1
