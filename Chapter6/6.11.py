def computeCommission(salesAmount):
    print()
    print("Sales Amount\t\t Commission")
    print()
    for i in range(10000,100001,5000):
        if 0.01 <= i <= 10000 :
            Commission = (i * 9 )/100

        elif 10000.01 <= i <= 15000 :
            Commission = (i * 10 )/100

        else :
            Commission = (i * 11.7 )/100
    
        print(i,"\t\t\t",format(Commission,"5.1f"))
        
        
def main() :
    
    salesAmount = eval(input("Plz enter Sales Amount : "))
    computeCommission(salesAmount)

main()
 
