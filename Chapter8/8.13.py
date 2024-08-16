def prefix(s1, s2):
    if s1 == s2 :
        print("Their common prefix : ",s1)

    else :
        i , j = 0 , 0
        dash = ""
        while s1[i]==s2[j] :
            dash = dash + s1[i]
            i += 1
            j += 1
            if s1[i]!=s2[j] :
                print("Their common prefix : ",dash)
            
def main():
    s1 = input("PLZ enter string one : ")
    s2 = input("PLZ enter string two : ")
    prefix(s1, s2)

main()
