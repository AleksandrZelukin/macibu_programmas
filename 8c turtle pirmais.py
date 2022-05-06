from turtle import *
def ts (a,b,x,y,z=4):
    penup()
    goto(x,y)
    pendown()
    pensize(z)
    fd (a)
    lt (90)
    fd(b)
    lt(90)
    fd(a)
    lt(90)
    fd(b)
    lt(90)

ts(50,100,-100,100,2)
ts(40,80,100,-100)
