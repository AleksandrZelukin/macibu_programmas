from turtle import *
from random import randint
speed(400)
bgcolor("pink")
pensize(4)
colormode(255)
def rinkis(x,y):
    up()
    goto(x,y)
    down()
    for i in range(6):
        r = (randint(0,255))
        g = (randint(0,255))
        b = (randint(0,255))
        color(r,g,b)
        circle(50)
        lt(60)
onscreenclick(rinkis)
done()