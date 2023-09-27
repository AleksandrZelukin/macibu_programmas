from turtle import *
a,x,y=150,150,20
def kvad(a,x,y):
    up()
    goto(x,y)
    down()
    for i in range(4):
        fd(a)
        lt(90)

kvad(a,x,y)
kvad(a+20,x-100,y-150)
kvad(-75,100,75)

mainloop()