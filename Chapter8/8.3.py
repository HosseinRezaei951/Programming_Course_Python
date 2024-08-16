def validpass(password):

    count = 0
    if len(password) >= 8 :
        
        if password.isalnum()== True:

        
            
            for i in range(0,len(password)+1):
                R = password[i] 
                if R.isdigit() :
                    count += 1
                    if count >= 2:
                        print("valid password")
                        break

        else :
            print("invalid password")

    else :
        print("invalid password")


def main():
    Pass = input("Enter a password : ")
    validpass(Pass)

main()

