year = eval(input("Plz enter a year : "))

first_day = eval(input("Plz enter the first day of the year ( 0=sunday , 1=monday , ... , 6=saturday ) : "))

# Check if the year is a leap year
isLeapYear = (year % 4 == 0 and year % 100 != 0) or  (year % 400 == 0)


    
count = first_day
for i in range(1,13):
    
    if i == 1 :
        count += 0
        print("January 1,",year,"is",end=" ")

    elif i == 2 :
        count += 31
        print("February 1,",year,"is",end=" ")

    elif i == 3 :
        if isLeapYear == True :
            count += 29

        else :
            count += 28
        print("March 1,",year,"is",end=" ")

    elif i == 4 :
        count += 31
        print("April 1,",year,"is",end=" ")

    elif i == 5 :
        count += 30
        print("May 1,",year,"is",end=" ")

    elif i == 6 :
        count += 31
        print("June 1,",year,"is",end=" ")

    elif i == 7 :
        count += 30
        print("July 1,",year,"is",end=" ")

    elif i == 8 :
        count += 31
        print("August 1,",year,"is",end=" ")

    elif i == 9 :
        count += 31
        print("September 1,",year,"is",end=" ")

    elif i == 10 :
        count += 30
        print("October 1,",year,"is",end=" ")

    elif i == 11 :
        count += 31
        print("November 1,",year,"is",end=" ")

    elif i == 12 :
        count += 30
        print("December 1,",year,"is",end=" ")

        
        
    if count % 7 == 0 :
        
        print("Sunday","\n")

    elif count % 7 == 1 :
        print("Monday","\n")

    elif count % 7 == 2 :
        print("Tuesday","\n")

    elif count % 7 == 3 :
        print("Wednesday","\n")

    elif count % 7 == 4 :
        print("Thursday","\n")

    elif count % 7 == 5 :
        print("Friday","\n")

    elif count % 7 == 6 :
        print("Saturday","\n")
        
        





    




