weight=eval(input("Enter weight in pounds:"))

height=eval(input("Enter height in pounds:"))

kilograms=weight*0.45359237

meters=height*0.0254

BMI=kilograms/(meters**2)

R=(round(BMI*10000))/10000

print("BMI is",R)
