subtotal,gratuity_rate=eval(input("Enter the subtotal and a gratuity rate:"))

gratuity_rate=(subtotal*gratuity_rate)/100

total=subtotal+gratuity_rate

print("The gratuity is",(int(gratuity_rate*100))/100,"and the total is",(int(total*100))/100)
