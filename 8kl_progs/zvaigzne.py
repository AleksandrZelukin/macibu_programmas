from turtle import *
from random import randint
stars = (-100,100,-150,-150,150,-150)
krasa = ("red","green","yellow","blue","pink")
atbilde=textinput("Jautājums", "Ko zimējam?")
if atbilde == "zvaigzne":
    for i in range(3):
        up()
        goto(stars[0+i],stars[1+i])
        down()
        lt(72)
        s = randint(0, 4)
        pencolor(krasa[s])
        write('zvaigzne Nr {}'.format(i+1),font=('Arial',24,'italic'))
        for i in range(5):
            forward(50)
            rt(144)
done()