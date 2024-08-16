amount = eval(input("Plz enter an amount : "))

annual_interest_rate = eval(input("Plz enter the annual interest rate : "))

number_of_months = eval(input("Plz enter the number of months : "))


value = 0
for i in range( 1 , number_of_months+1 ) :

    value = (value + amount)  * (1 + (annual_interest_rate/1200) )
    
print("After ",number_of_months,"months your account value is : ",format(value,".3f"))
    
