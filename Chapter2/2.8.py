M=eval(input("Enter the amount of water in kilograms:"))

initialtemperature=eval(input("Enter the initial temperature:"))

finaltemperature=eval(input("Enter the final temperature:"))

Q=M*(finaltemperature-initialtemperature)*4184

print("The energy needed is",Q)
