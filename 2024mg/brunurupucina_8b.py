from turtle import *

t = Turtle()
t.shape("turtle")
t.pensize(4)
krasa = ("red","blue","yellow","brown","orange","navy")


def figura(x,y,z,n,k):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.fillcolor(krasa[k])
    t.begin_fill()
    for i in range(n):
        t.fd(z)
        t.lt(360/n)
    t.end_fill()

def saule(x,y,z,k=2):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.fillcolor(krasa[k])
    t.pencolor(krasa[k])
    t.begin_fill()
    for i in range(12):
        t.fd(z)
        t.bk(z)
        t.lt(30)
    t.end_fill()

siena = figura(-200,-380,300,4,3)
durvis = figura(-80,-380,80,4,5)
jumta = figura(-225,-80,350,3,1)
sun = saule(-200,300,200)
