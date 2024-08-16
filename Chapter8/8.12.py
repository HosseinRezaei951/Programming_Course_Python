genome = input("Enter a genome string : ")
Length = len(genome)
s = 0
flag = False 
for i in range(0,Length+1):
    t = genome[i:i+3]

    if t == "ATG" :
        s = i + 3

    elif (t == "TAG" or  t == "TAA" or t == "TGA") :
        gene = genome[s:i]

        if len(gene) % 3 == 0 :
            print(gene)
            flag = True

if flag == False :
    print("no gene is found")
            
        
