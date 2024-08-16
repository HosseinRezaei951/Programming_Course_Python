i = 0
A = 1
B = 3

while A <= 97 and B <= 99 :

    i = i + (A / B)

    A += 2
    B += 2

print("sum the following series : \n"
      " \t 1/3 + 3/5 + ... + 97/99 = "+str(i))

