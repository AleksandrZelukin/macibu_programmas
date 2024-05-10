from turtle import *
speed(1000)
y = -350
color("brown")
for m in range(24):
    if m % 2 == 0:
        x = -450
        z = 16
    else:
        x = -425
        z = 15
    for k in range(z):
        up()
        setposition(x,y)
        down()
        begin_fill()
        for i in range(2):
            fd(50)
            rt(90)
            fd(25)
            rt(90)
        end_fill()
        x += 55
    y += 30



done()