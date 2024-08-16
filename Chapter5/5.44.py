num = eval(input("PLz enter a decimal integer : "))
r = ""
while num // 2 > 0 :

    r = str(num % 2)+r
    num = num // 2

print(str(num)+r,end="")
