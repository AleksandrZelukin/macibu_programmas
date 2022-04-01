from turtle import *

a=Turtle()

def kvadrat(x,y,size):
    a.penup()
    a.goto(x,y)
    a.pendown()
    for i in range(4):
        a.fd(size)
        a.lt(90)



kvadrat(-100,-100,200)
