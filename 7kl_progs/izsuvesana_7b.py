from turtle import *
speed(500)
pensize(6)
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
x=100
y=100
step = 10
for s in range (6):
    for n in range(step):   
        up()
        goto(x,y)
        down()
        krustins()
        x -= 35
    for k in range(step):
        up()
        goto(x,y)
        down()
        krustins()
        y -= 35    
    for n in range(step):   
        up()
        goto(x,y)
        down()
        krustins()
        x += 35    
    for k in range(step):
        up()
        goto(x,y)
        down()
        krustins()
        y += 35
    step -=2
    x -= 35
    y -= 35               
done()