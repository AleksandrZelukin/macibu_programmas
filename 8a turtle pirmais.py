from turtle import *

col=["red","blue","yellow","darkred"]
shape("turtle")

def f (x,y,a,s,z,q):
    penup()
    goto(x,y)
    color(col[q])
    pensize(z)
    pendown()
    for i in range (s):
        fd(a)
        lt(360/s)
        i += 1
        
    
f(-100,-200,30,4,6,0)
f(100,200,40,8,4,3)
f(0,0,4,96,2,2)
