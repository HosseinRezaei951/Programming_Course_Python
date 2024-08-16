def area(s):
    import math
    Area = (5*(s**2))/(4*(math.tan(math.pi/5)))
    return Area

def main():
    side = eval(input("Enter the side : "))
    print("The area of the pentagon is",area(side))

main()
