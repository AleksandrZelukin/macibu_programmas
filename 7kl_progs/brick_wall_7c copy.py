from turtle import *
speed(1000)
def briks ():
    for i in range(2):
        fd(50)
        rt(90)
        fd(25)
        rt(90)

y = -350
color("brown")
x = -450
for k in range(16):
    up()
    setposition(x,y)
    down()
    begin_fill()
    briks()
    end_fill()
    x += 55




done()