month = eval(input("Enter the month : "))

year = eval(input("Enter the year : "))


#1            
if month == 1 :
            print("January",year,"has 31 days")

if month == 2 :
            if ( (year % 4 == 0 and year % 100 != 0) or \
                 (year % 400 == 0) ) :
                        print("February",year,"has 29 days")
            else :
                        print("February",year,"has 28 days")
                        
if month == 3 :
            print("March",year,"has 31 days")

                        
#2
if month == 4 :
            print("April",year,"has 30 days")

if month == 5 :
            print("May",year,"has 31 days")

if month == 6 :
            print("June",year,"has 30 days")            


#3
if month == 7 :
            print("July",year,"has 31 days")

if month == 8 :
            print("August",year,"has 31 days")

if month == 9 :
            print("September",year,"has 30 days")


#4
if month == 10 :
            print("October",year,"has 31 days")

if month == 11 :
            print("November",year,"has 30 days")

if month == 12 :
            print("December",year,"has 31 days")
