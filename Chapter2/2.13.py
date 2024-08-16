integer=eval(input("Enter an integer:"))

p1=int(integer/1000)

Remaining1=integer-(p1*1000)

p2=int(Remaining1/100)

Remaining2=integer-((p1*1000)+(p2*100))

p3=int(Remaining2/10)

Remaining3=integer-((p1*1000)+(p2*100)+(p3*10))

p4=int(Remaining3/1)

print(p1)

print(p2)

print(p3)

print(p4)
