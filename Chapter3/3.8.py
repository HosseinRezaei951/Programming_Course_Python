amount = eval(input("Enter an amount(for example 1156):"))

remainingAmount = amount

numberOfOneDollars = remainingAmount // 100
cents = remainingAmount % 100

print("Your amount", amount, "consists of\n",
      "\t", numberOfOneDollars, "dollars\n",
      "\t", cents, "cents")
