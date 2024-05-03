from turtle import *
from random import randint

for k in range (50):
    up()
    x=randint(-300,300)
    y=randint(-300,300)
    goto(x,y)
    down()
    for i in range (5):
        fd(50)
        lt(144)
    
done()