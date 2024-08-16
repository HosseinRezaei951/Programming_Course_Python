NUMBER_OF_PRIMES = 50
NUMBER_OF_PRIMES_PER_LINE = 10
count = 0
number = 2
lst = [] 
print("The first 50 prime numbers are")

while count < NUMBER_OF_PRIMES:
    
    isPrime = True
    divisor = 2
    
    while divisor <= (number ** 0.5):
        if number % divisor == 0:
            isPrime = False
            break
        divisor += 1
    if isPrime :
        lst.append(number)
        count += 1
    number += 1
    
for i in range(len(lst)):
    print(format(lst[i], "5d"), end = '')
    count += 1
    if count % NUMBER_OF_PRIMES_PER_LINE == 0:
            print()
