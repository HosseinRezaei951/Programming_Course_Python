w1,p1 = eval(input("Enter weight and price for package 1: "))
w2,p2 = eval(input("Enter weight and price for package 2: "))


Price_per_kilo1 = p1 / w1
Price_per_kilo2 = p2 / w2

if p1 == p2 :
            if w1 > w2 :
                        print ("Package 1 has the better price.")

            elif w2 > w1 :
                        print ("Package 2 has the better price.")

elif w1 == w2 :
            if p1 < p2 :
                        print ("Package 1 has the better price.")

            elif p2 < p1 :
                        print ("Package 2 has the better price.")

elif Price_per_kilo1 > Price_per_kilo2 :
            print ("Package 1 has the better price.")

elif Price_per_kilo2 > Price_per_kilo1 :
            print ("Package 2 has the better price.")


