from turtle import *

t = Turtle()


t.screen.setup(800, 800)
t.screen.bgcolor("orange")

t.shape("turtle")
t.color("blue")
t.stamp()
t.color("red")

t.up()
t.goto(-100,100)
t.down()
t.fd(200)

def rectangle(w, h):
    for i in range(2):
        t.left(90)
        t.fd(h)
        t.left(90)
        t.fd(w)        
rectangle(320, 200)

def sq_cr(side):
    for i in range(4):
        t.left(90)
        t.fd(side)
    t.bk(side / 2)
    t.circle(side / 2, 360)
    t.left(180)
    t.circle(side / 2, 360)
sq_cr(250)


def circ(d, r, rBig):
    for i in range(d):
        t.circle(rBig, 360 / d)
        t.dot(r, "red")
t.up()
t.goto(350, 0)
t.setheading(90)
t.down()
circ(45, 10, 350)


t.up()
t.goto(-450, 0)
t.down()
t.setheading(270)
for i in range(5):
    t.circle(50, 180)
    t.begin_fill()
    t.circle(-50, 180)
    t.end_fill() 




t.screen.exitonclick()
t.screen.mainloop()
