balance,interest_rate=eval(input("Enter balance and interest rate (e.g., 3 for 3%):"))

interest=balance*(interest_rate/1200)

R=(round(interest*100000))/100000

print("The interest is",R)
