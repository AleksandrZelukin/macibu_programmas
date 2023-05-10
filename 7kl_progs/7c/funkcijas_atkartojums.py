from turtle import *
def kvad(a,x,y):
    up()
    goto(x,y)
    down()
    for i in range(4):
        fd(a)
        lt(90)



kvad(150,150,20)
kvad(50,-150,50)
kvad(-75,100,75)

mainloop()