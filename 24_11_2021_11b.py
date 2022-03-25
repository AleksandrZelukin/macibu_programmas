from turtle import *
b=Turtle()
#b.screen.setup(800,800)
b.shape("turtle")
b.pensize(4)

def fig (x,y):
    b.up()
    b.goto(x,y)
    b.down()
    b.goto(-x,y)
    b.goto(-x,-y)
    b.goto(x,-y)
    b.goto(x,y)
    b.up()
    b.goto(0,-y)
    b.down()
    b.fillcolor("yellow")
    b.begin_fill()
    b.circle(x,360)
    b.end_fill()

def figura (x,a,y,l):
    b.up()
    b.goto(x,y)
    b.down()
    b.left(a)
    b.forward(l)
    b.left(a)
    b.forward(l)
    b.left(a)
    b.forward(l)
    b.left(a)
    b.forward(l)
    

fig(150,150)
fig(100,100)
fig(50,50)
fig(25,25)



figura(0,90,0,20)
figura(150,90,150,200)
figura(-150,90,-150,100)
figura(15,90,150,40)
figura(25,90,-150,30)
figura(-15,90,-15,35)



b.screen.exitonclick()

