year = eval(input("Enter year: (e.g., 2008): "))

month = eval(input("Enter month(1-12): "))

day_of_the_month = eval(input("Enter the day of the month(1-31): "))

if (month == 1) :
            month = 13
            year = year - 1 

            q = day_of_the_month
            m = month
            j = (year//100)
            k = (year % 100)

            h = ( q + ((26*(m+1))//10) + k + (k//4) + (j//4) + (5*j) ) % 7

            if h == 0 :
                        print("Day of the week is Saturday")
            elif h == 1 :
                        print("Day of the week is Sunday")
            elif h == 2 :
                        print("Day of the week is Monday")
            elif h == 3 :
                        print("Day of the week is Tuesday")
            elif h == 4 :
                        print("Day of the week is Wednesday")
            elif h == 5 :
                        print("Day of the week is Thursday")
            elif h == 6 :
                        print("Day of the week is Friday")
            
elif (month == 2) :
            month = 14
            year = year - 1

            q = day_of_the_month
            m = month
            j = (year//100)
            k = (year % 100)

            h = ( q + ((26*(m+1))//10) + k + (k//4) + (j//4) + (5*j) ) % 7

            if h == 0 :
                        print("Day of the week is Saturday")
            elif h == 1 :
                        print("Day of the week is Sunday")
            elif h == 2 :
                        print("Day of the week is Monday")
            elif h == 3 :
                        print("Day of the week is Tuesday")
            elif h == 4 :
                        print("Day of the week is Wednesday")
            elif h == 5 :
                        print("Day of the week is Thursday")
            elif h == 6 :
                        print("Day of the week is Friday")
            
            
else :
            q = day_of_the_month
            m = month
            j = (year//100)
            k = (year % 100)

            h = ( q + ((26*(m+1))//10) + k + (k//4) + (j//4) + (5*j) ) % 7

            if h == 0 :
                        print("Day of the week is Saturday")
            elif h == 1 :
                        print("Day of the week is Sunday")
            elif h == 2 :
                        print("Day of the week is Monday")
            elif h == 3 :
                        print("Day of the week is Tuesday")
            elif h == 4 :
                        print("Day of the week is Wednesday")
            elif h == 5 :
                        print("Day of the week is Thursday")
            elif h == 6 :
                        print("Day of the week is Friday")


