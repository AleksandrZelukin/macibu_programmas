from turtle import *
from random import randint



for i in range (50):
    up()
    goto(randint(-300,300),randint(-300,300))
    down()
    bgcolor("blue")
    color("yellow")
    fillcolor("yellow")
    m = randint(20,70)
    begin_fill()

    for k in range(5):
        
        fd(m)
        rt(144)
    end_fill()
done()