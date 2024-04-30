from turtle import *
from random import randint,choice
speed(300)
colormode(255)
bgcolor(0,0,110)
color((255,255,0),(255,255,0))
grad = [0,30,90,45]
for k in range(40):
    x = randint(-300,300)
    y = randint(-300,300)
    m = randint(10,50)
    g = choice(grad)
    up()
    setposition(x,y)
    down()
    lt(g)
    begin_fill()
    for i in range (5):
        
        fd(m)
        lt(144)
    end_fill()
up()
home()
down()
import namins_7b
done()