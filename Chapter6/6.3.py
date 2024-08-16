def reverse(number):
    p1 = number // 100
    R1 = number % 100

    P2 = R1 // 10
    p3 = R1 % 10

    if p1 == p3 :
        return True
    else :
        return False

def isPalindrome(answer):
    if answer == True :
        print("The integer is a palindrome.")

    elif answer == False :
        print("The integer is not a palindrome.")

def main():
    number = eval(input("Plz enter an integer : "))
    answer = reverse(number)
    
    return isPalindrome(answer)


main()
    
