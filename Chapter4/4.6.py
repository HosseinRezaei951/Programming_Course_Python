weight = eval(input("Enter weight in pounds: "))

feet = eval(input("Enter feet: "))
inches = eval(input("Enter inches: "))


KILOGRAMS_PER_POUND = 0.45359237 
METERS_PER_INCH = 0.0254 
METERS_PER_Feet = 0.3048

weightInKilograms = weight * KILOGRAMS_PER_POUND
inchesInMeters = inches * METERS_PER_INCH
FeetInMeters = feet * METERS_PER_Feet

heightInMeters = FeetInMeters + inchesInMeters

bmi = weightInKilograms / (heightInMeters ** 2)


print("BMI is ", bmi)
if bmi < 18.5:
 print("Underweight")
elif bmi < 25:
 print("Normal")
elif bmi < 30:
 print("Overweight")
else:
 print("Obese")
