def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        
        if number % divisor == 0:
            return False 
        divisor += 1

    return True # number is prime


def printPrimeNumbers(numberOfPrimes):
    last_prime = 2
    NUMBER_OF_PRIMES = numberOfPrimes # Number of primes to display
    count = 0 # Count the number of prime numbers
    number = 2 # A number to be tested for primeness

    # Repeatedly find prime numbers
    while count < NUMBER_OF_PRIMES:

        # Print the prime number and increase the count
        
        if isPrime(number) == True :
            
            count += 1 # Increase the count
            if number - last_prime == 2 :
                print("(",last_prime,",",number,")")

            last_prime = number

        # Check if the next number is prime
        
        number += 1
 
def main():
    print("The first 1000 prime numbers are")
    printPrimeNumbers(1000)

main()
