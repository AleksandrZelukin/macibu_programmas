from turtle import *
pensize(4)
def krustins():
    lt(45)
    fd(50)
    up()
    lt(135)
    fd(35)
    lt(135)
    down()
    fd(50)
    lt(45)
x,y = 0, 0
for i in range(5):
    y += 40
    x = 0
    for j in range(5):
        up()
        goto(x,y)
        down()
        x += -40 
        krustins()

done()