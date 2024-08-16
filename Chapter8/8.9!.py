def BinaryTodecimal(value):
    LEN = len(value)
    i = LEN-1
    s = 0
    count = 0
    while count < LEN :
        R = eval(value[i])
        s = s + (R *(2**(i+1)))
        count += 1
        i -= 1

    return str(s)
        
def decimalToHex(value):
    LEN = len(value)
    i = LEN-1
    s = 0
    count = 0
    while count < LEN :
        R = eval(value[i])
        s = s + (R *(16**(i+1)))
        count += 1
        i -= 1

    if s == 10 :
        print(A)

    elif s == 11 :
        print(B)

    elif s == 12 :
        print(C)
        
    elif s == 13 :
        print(D)
        
    elif s == 14 :
        print(E)
        
    elif s == 15 :
        print(F)
    
        
        

def main():
    num = input("Enter a binary number : ")
    decimalToHex(BinaryTodecimal(num))

main()
