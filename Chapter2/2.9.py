temperature=eval(input("Enter the temperature in Fahrenheit between -58 and 41:"))

speed=eval(input("Enter the wind speed in miles per hour:"))

twc=35.74+(0.6215*temperature)-(35.75*(speed**0.16))+(0.4275*temperature*(speed**0.16))

final=((twc*100000)//1)/100000

print("The wind chill index is",final)


