amount = eval(input("Enter an amount, for example, 11.56: "))


remainingAmount = int(amount * 100)

numberOfOneDollars = remainingAmount // 100
remainingAmount = remainingAmount % 100

if numberOfOneDollars > 0 :
            if numberOfOneDollars == 1 :
                        print("Your amount", amount, "consists of\n",
                              "\t","one dollars" )
                        
            else :
                        print("Your amount", amount, "consists of\n",
                              "\t", numberOfOneDollars, "dollars")
                       

numberOfQuarters = remainingAmount // 25
remainingAmount = remainingAmount % 25

if numberOfQuarters > 0 :
            if numberOfQuarters == 1 :
                        print("\t", "one quarters")
                        
            else :
                        print("\t", numberOfQuarters, "quarters")


numberOfDimes = remainingAmount // 10
remainingAmount = remainingAmount % 10

if numberOfDimes > 0 :
            if numberOfDimes == 1 :
                        print("\t", " one dimes")
                        
            else :
                        print("\t", numberOfDimes, "dimes")


numberOfNickels = remainingAmount // 5
remainingAmount = remainingAmount % 5

if numberOfNickels > 0 :
            if numberOfNickels == 1 :
                        print("\t", " one nickels")
                        
            else :
                        print("\t", numberOfNickels, "nickels")


numberOfPennies = remainingAmount

if numberOfPennies > 0 :
            if numberOfPennies == 1 :
                        print("\t", " one pennies")

            else :
                        print("\t", numberOfPennies, "pennies")   
            
