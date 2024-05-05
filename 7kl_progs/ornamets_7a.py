from turtle import *
from random import randint
speed(400)
bgcolor("pink")
pensize(1)
colormode(255)

for i in range(36):
    r = (randint(0,255))
    g = (randint(0,255))
    b = (randint(0,255))
    color(r,g,b)
    circle(100,360,8)
    lt(10)

done()