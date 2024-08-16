speed,acceleration=eval(input("Enter speed and acceleration:"))

#Formula:length=(speed**2)/(2*acceleration)

up=speed**2

down=2*acceleration

length=(round((up/down)*1000))/1000

print("The minimum runway length for this airplane is",length,"meters")
