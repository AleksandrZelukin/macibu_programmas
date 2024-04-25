from turtle import *
from random import randint
speed(1400)
pensize(2)
krasa = ["orange","blue","red","yellow","brown","green","tomato","coral"]

for i in range(18):
    num = randint(0,7)
    krasa4 = krasa[num]
    pencolor(krasa4)
    circle(100)
    lt(20)

lt(10)
for j in range(18):

    for m in range(4):
        num = randint(0,7)
        krasa4 = krasa[num]
        pencolor(krasa4)
        fd(150)
        lt(90)
    lt(20)
done()