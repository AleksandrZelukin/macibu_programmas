from turtle import *
import tkinter
speed(1000)
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
def siena():
    figuri(-100,-320,4,200,1)
def jumta():
    figuri(-125,-120,3,250,4)
def durvis():
    figuri(-80,-320,4,100,7)
def s():
    saule(-200,200,200)
poga1 = tkinter.Button(text="SIENA",command=siena)
poga1.place(relx=.10,rely=.10)
poga2 = tkinter.Button(text="DURVIS",command=durvis)
poga2.place(relx=.30,rely=.10)
poga3 = tkinter.Button(text="JUMTA",command=jumta)
poga3.place(relx=.50,rely=.10)
poga4 = tkinter.Button(text="SAULE",command=s)
poga4.place(relx=.7,rely=.10)
mainloop()