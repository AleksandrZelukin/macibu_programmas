from turtle import *

def kvad(x,y,z,q):
    up()
    goto(x,y)
    down()
    fillcolor(q)
    begin_fill()
    for i in range(4):
        fd(z)
        lt(90)
    end_fill()

kvad(100,100,200,'red')
kvad(-100,-100,150,'blue')
kvad(-250,-250,75,'lightgreen')
mainloop()