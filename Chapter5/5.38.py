import time

sec = eval(input("Plz enter the number of seconds : "))
T = sec - 1

while T != 0 :
    time.sleep(1)
    print(T,"seconds remaining")
    T -= 1

if T == 0 :
    time.sleep(1)
    print("Stopped")
