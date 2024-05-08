from turtle import *
from random import randint
colormode(255)
speed(500)

def fig (x,y):
    up()
    goto(x,y)
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    color(r,g,b)
    begin_fill()
    down()
    n = randint(30,50)   
    #for i in range (n):
    #   fd(50)
    #    lt(360/n)
    #write(position())
    circle(n)
    end_fill()   
        
onscreenclick(fig)

done()