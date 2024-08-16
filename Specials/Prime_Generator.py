def prime ( num ) :

    m = 2
    while m < num :
        flag =  False
        i = 2

        while i <= (m**0.5) and flag == False :
            r = m % i
            if r == 0 :
                flag = True

            i += 1

        if flag == False :
            print(m,end=" ")

        m += 1

        


def main() :

    num = eval(input("Plz enter a number : "))
    prime(num) 

main()
