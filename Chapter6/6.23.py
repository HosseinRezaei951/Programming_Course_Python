def convertMillis(millis):
    seconds = millis / 1000
    
    hours = seconds // 3600    
    r1 = seconds % 3600
    
    minutes = r1 // 60
    r2 = r1 % 60

    seconds = r2
    print("The",millis,"milliseconds is ",int(hours),":",int(minutes),":",int(seconds))
    

def main():
    
    millis = eval(input("PLZ enter a value for milliseconds : "))
    convertMillis(millis)
    

main()
    
    
