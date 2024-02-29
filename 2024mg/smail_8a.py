from turtle import *
speed(10)
pensize(4)

def go(x,y):
    pu()
    goto(x,y)
    pd()
    seth(0)
    
go(-250,0)
circle(100)
go(-330,100)
rt(90)
circle(80,180)
go(-300,140)
dot()
go(-200,140)
dot()

go(250,0)
circle(100)

go(310,40)
rt(270)
circle(60,180)
go(300,140)
dot()
go(200,140)
dot()

go(0,0)
write("Sveiciens no 8.a klase!",font=("Arial",28,"bold"),align="center")


