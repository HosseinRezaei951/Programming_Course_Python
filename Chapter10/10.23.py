def solveQuadratic(eqn, roots):
    a = eqn[0]
    b = eqn[1]
    c = eqn[2]
    
    r1 = ((-b)+((roots)**0.5))/(2*a)
    r2 = ((-b)-((roots)**0.5))/(2*a)
    r3 = (-b)/2*a
    
    if roots > 0 :
          print("The roots are",((int(r1*1000000))/1000000),"and",((int(r2*100000))/100000))
          print("The quadratic equation have 2 roots.")
    elif roots == 0 :
          print("The roots is",r3)
          print("The quadratic equation have 1 roots.")
    elif roots < 0 :
          print("The equation has no real roots.")
          print("The quadratic equation have no roots.")
  
def main():
    lst = []
    item = input("Enter a score : ")
    List = item.split()
    lst = [eval(x) for x in List]
    a = lst[0]
    b = lst[1]
    c = lst[2]
    eqn =[]
    for i in range(0,3):
       eqn.append(lst[i]) 
    roots = ((pow(b,2))-(4*a*c))
    solveQuadratic(eqn, roots)
    
    
main()    
