import time

currentTime = time.time() 

H=0

M=0

H,M=eval(input("Enter the time zone offset to GMT(Ex:3,30):"))


totalSeconds = int(currentTime)


currentSecond = totalSeconds % 60 


totalMinutes =((totalSeconds )// 60) 


currentMinute = (totalMinutes+ M) % 60


totalHours = totalMinutes // 60


currentHour = ((totalHours+H)% 24)

if ( 12 > currentHour >= 0 ):

            print("The current time is",currentHour,":",currentMinute,":",currentSecond,"AM")

elif ( 13 <= currentHour <= 23):
            currentHour = currentHour-12
            print("The current time is",currentHour,":",currentMinute,":",currentSecond,"PM")

