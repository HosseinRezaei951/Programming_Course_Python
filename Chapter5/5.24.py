import math

balance = eval(input("Loan Amount: "))

Number_Of_Years = eval(input("Number of Years: "))

Annual_Interest_Rate = eval(input("Annual Interest Rate: "))
print()

Monthly_Interest_Rate = Annual_Interest_Rate/1200

Number_Of_Month = Number_Of_Years*12

Monthly_Payment = balance * Monthly_Interest_Rate / (1- 1/(1 + Monthly_Interest_Rate) ** (Number_Of_Years * 12)) #listing 2.8

Monthly_Interest = Monthly_Interest_Rate * Number_Of_Month

Total_Payment = Monthly_Payment * Number_Of_Years * 12


print("Monthly Payment: ",format(Monthly_Payment,".2f"))
print("Total Payment: ",format(Total_Payment,".2f"))
print()


print("Payment#","\t","Interest","\t\t","Principal","\t\t","Balance")
for i in range(1,(Number_Of_Years*12)+1):


    interest = Monthly_Interest_Rate*balance
    principal = Monthly_Payment-interest
    balance = balance-principal
    
    
    print(str(i)+"\t\t",format(interest,".2f"),"  \t\t",format(principal,".2f"),"\t\t",format(balance,".2f"))
