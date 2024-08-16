import turtle

n = " "
turtle.penup()
turtle.goto(-50,100)


for i in range(1,11):

    turtle.pendown()
    n = str(n+" ")+str(i) 
    turtle.write(str(n),font=(24))
    turtle.penup()
    turtle.goto(-50,(100-(20*i)))
