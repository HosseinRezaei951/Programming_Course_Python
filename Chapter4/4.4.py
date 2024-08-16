import random

num1 = random.randint(0,99)
num2 = random.randint(0,99)

answer = eval(input('What is '+str(num1)+"+"+str(num2)+' ? '))

if answer == (num1+num2) :
      print("The answer is correct")
else :
      print("The answer is false")
