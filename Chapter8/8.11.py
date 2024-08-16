def reverse(s):
    
    R = len(s)
    dash = ""
    while R > 0 :
        dash = dash + s[R-1]
        R -= 1

    print(dash)

def main():
    s = input("Plz enter a string : ")
    reverse(s)
main()
