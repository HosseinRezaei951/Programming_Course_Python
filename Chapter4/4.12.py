intiger = eval(input("Enter an integer: "))


print( "Is",intiger,"divisible by 5 and 6?" ,\
      ((intiger % 5 == 0 ) and (intiger % 6 == 0 )) )

print( "Is",intiger,"divisible by 5 or 6?" ,\
       ((intiger % 5 == 0 ) or (intiger % 6 == 0 )) )

print( "Is",intiger,"divisible by 5 or 6, but not both?" ,\
       ((intiger % 5 == 0 ) or (intiger % 6 == 0 ) and( not((intiger % 5 == 0 ) and (intiger % 6 == 0 )) ) ) )
