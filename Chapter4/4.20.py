temperature = eval(input("Enter the temperature in Fahrenheit between -58 and 41: "))

speed = eval(input("Enter the wind speed in miles per hour(greater than or equal to 2): "))

A = 35.74
B = 0.6215
C = 35.75
D = 0.4275

if ((temperature>(-58)) and (temperature<(41)) and (speed>=(2))):
            part1 = (A + (B * temperature))
            part2 = (-(C * (speed**0.16))) + (D * temperature * (speed**0.16))

            Twc = part1 + part2
            print("The wind chill index is ",Twc)

            
elif ((temperature>(-58)) and (temperature<(41)) and (not(speed>=(2))) ):
             print("the wind speed is invalid.")

elif ((temperature>(-58)) or (temperature<(41)) and (speed>=(2)) ):
             print("the temperature is invalid.")


else :
             print("the temperature and wind speed are invalid")
