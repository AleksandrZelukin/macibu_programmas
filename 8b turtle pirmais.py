from turtle import *


def fig(x,y,a,s,z=4):
    pensize(z)
    penup()
    goto(x,y)
    pendown()
    for i in range(s):
        fd(a)
        lt(360/s)
        i += 1

fig(-100,100,5,48,2)
fig(100,-100,120,5,8)

