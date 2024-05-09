from turtle import *
speed(1000)
y=-350
color("brown")
for m in range(16):
    if m% 2 == 0:
        x=-450
    else:
        x=-425   
    for k in range (16):
        up()
        goto(x,y)
        down()
        begin_fill()
        for i in range (2):
            fd(50)
            rt(90)
            fd(25)
            rt(90)
        end_fill()
        x += 55
    y += 30
done()    