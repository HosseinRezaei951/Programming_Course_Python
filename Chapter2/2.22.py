number_of_years=eval(input("Enter the number of years:"))

current_population=312032486

seconds=(number_of_years*365*24*60*60)

birth=(seconds//7)

death=(seconds//13)

immigrant=(seconds//45)

population=(current_population+birth+immigrant)-(death)

print("The population in 5 years is",population)
