from turtle import *
from random import randint
speed(100)
pensize(2)
for m in range (12):
    up()
    goto(randint(-200,200),randint(-100,100))
    down()
    for i in range(36):
        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)
        colormode(255)
        color(r,g,b)
        circle(50)
        lt(10)
    

done()