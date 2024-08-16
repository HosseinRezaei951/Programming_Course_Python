investment_amount=eval(input("Enter investment amount:"))

annual_interest_rate=eval(input("Enter annual interest rate:"))

years=eval(input("Enter number of years:"))

number_of_months=years*12

monthly_interest_rate=(annual_interest_rate/100)/12

future_investment_value=investment_amount*((1+monthly_interest_rate)**number_of_months)

print("Accumulated value is",(int(future_investment_value*100)/100))

                                           
                                           
