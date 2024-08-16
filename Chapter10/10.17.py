def isAnagram(s1 , s2):
    lst1 = []
    lst2 = []
    A = s1[0]
    B = s2[0]
    Len1 = len(A)
    Len2 = len(B)
    count = 0
    for i in range(0,Len1):
        for j in range(0,Len2):
            if A[i] == B[j] :
                count += 1
    if s1 == s2 :
        print(str(A),"and",str(B),"is an anagram")
    elif count == (Len1) :
        print(str(A),"and",str(B),"is an anagram")

    else :
        print(str(A),"and",str(B),"is not an anagram")
        
    
def main():
    lst1 = []
    lst2 = []
    lst = []
    for i in range(1,3):
        
        String = input("Enter a strings : ")
        List = String.split()
        lst = [str(x) for x in List]
        
        if i== 1 :
            lst1.append(lst[i-1])
        else :
            lst2.append(lst[i-2])
    isAnagram(lst1 , lst2)
    
        

main()
