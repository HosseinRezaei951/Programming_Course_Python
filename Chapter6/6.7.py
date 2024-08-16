def futureInvestmentValue(investmentAmount, monthlyInterestRate, years):
    numberOfMonths = years*12
    futureInvestmentValue = investmentAmount * ((1+ monthlyInterestRate)**numberOfMonths)
    print(format(futureInvestmentValue,".2f"))

def main():
    investmentAmount= eval(input("The amount invested : "))
    annualInterestRate = eval(input("Annual interest rate : "))
    monthlyInterestRate = (annualInterestRate/100)/12
    
    print("Years\tFuture Value")
    for i in range(1,31):
        print(i,"\t",end="")
        futureInvestmentValue(investmentAmount, monthlyInterestRate, i)

main()
    
    
