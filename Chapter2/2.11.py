final_account_value=eval(input("Enter final account value:"))

interest_rate_in_percent=eval(input("Enter annual interest rate in percent:"))

years=eval(input("Enter number of years:"))

monthly_interest_rate=(interest_rate_in_percent/100)/12

number_of_months=years*12

initial_deposit_amount=(final_account_value)/((1+monthly_interest_rate)**number_of_months)



print("Initial deposit value is",initial_deposit_amount)

