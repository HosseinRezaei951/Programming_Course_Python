year = eval(input("Enter a year: "))
zodiacYear = year % 12
lst = ["monkey","rooster","dog","pig","rat","ox","tiger","rabbit","dragon","snake","horse","sheep"]

for i in range(0,len(lst)):
    if i == zodiacYear :
        print(lst[i])
