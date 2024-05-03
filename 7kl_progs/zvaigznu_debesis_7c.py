from turtle import *
from random import randint, choice
speed(400)
for i in range (50):
    up()
    goto(randint(-300,300),randint(-300,300))
    down()
    colormode(255)
    bgcolor(0,0,80)
    color(255,255,0)
    fillcolor(255,255,170)
    g = [30,45,10,90]
    lt(choice(g))
    m = randint(10,40)
    begin_fill()
    for k in range(5):
        fd(m)
        rt(144)
    end_fill()
up()
setposition(-300,300)
lt(160)
down()
begin_fill()
circle(90,190)
end_fill()
done()