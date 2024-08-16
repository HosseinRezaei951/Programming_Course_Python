minutes=eval(input("Enter the number of minutes:"))

years=int(minutes/(60*24*365))

remainingminutes=minutes-(years*(60*24*365))

days=int(remainingminutes/(60*24))

print(minutes,"minutes is approximately",years,"years and",days,"days")
