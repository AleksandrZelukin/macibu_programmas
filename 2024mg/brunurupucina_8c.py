from turtle import *
shape("turtle")
pensize(4)
pencolor("blue")
krasa = ["black","red","yellow","blue","brown","orange","pink","lightblue"]
def figuri(x,y,n,k,m=0):
    pu()
    goto(x,y)
    pencolor(krasa[m])
    pd()
    ht()
    fillcolor(krasa[m])
    begin_fill()
    for i in range(n):
        forward(k)
        left(360/n)
    end_fill()
def saule(x,y,k,m=2):
    pu()
    goto(x,y)
    pencolor(krasa[m])
    pd()
    speed(1000)
    fillcolor(krasa[m])
    begin_fill()
    for i in range(18):
        fd(k)
        bk(k)
        lt(20)
    end_fill()
siena = figuri(-100,-320,4,200,1)
jumta = figuri(-125,-120,3,250,4)
durvis = figuri(-80,-320,4,100,7)
s = saule(-200,200,200)
