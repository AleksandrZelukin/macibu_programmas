from turtle import*
hideturtle()
up()
goto(-100,0)
down()
showturtle()
speed(2)
n=8
for x in range(n):
    fd(200)
    lt(180)
    rt(360/n)
   
    dot()

mainloop()