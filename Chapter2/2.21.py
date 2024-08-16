monthly_saving_amount=eval(input("Enter the monthly saving amount:"))

month1=monthly_saving_amount*(1 + 0.00417)

month2=(monthly_saving_amount+month1)*(1 + 0.00417)

month3=(monthly_saving_amount+month2)*(1 + 0.00417)

month4=(monthly_saving_amount+month3)*(1 + 0.00417)

month5=(monthly_saving_amount+month4)*(1 + 0.00417)

month6=(monthly_saving_amount+month5)*(1 + 0.00417)

print("After the sixth month, the account value is",(int(month6*100))/100)
