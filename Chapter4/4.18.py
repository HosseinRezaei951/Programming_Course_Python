ExchangeRate = eval(input("Enter the exchange rate from dollars to RMB : "))

user = eval(input("Enter 0 to convert dollars to RMB and 1 vice versa : "))

if (user == 0) :
    dollar = float(eval(input("Enter thedollor amount : ")))
    
    yuan = ExchangeRate * dollar
    
    print('$'+str(dollar),'is',float(yuan),'yuan')
    
elif (user == 1) :
    RMB = eval(input("Enter the RMB amount : "))
    
    dollar2 = RMB / ExchangeRate
    Result = (round(dollar2*100))/100
    
    print(float(RMB),"yuan is $",Result)

elif (user > 1) :
    print("Incorrect input")
    
