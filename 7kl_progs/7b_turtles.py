from turtle import *

a = Turtle()

a.shape("turtle")
a.pencolor("red")
a.color("red")
a.pensize(4)
a.fillcolor("lightblue")

a.begin_fill()
for i in range(4):
    a.fd(200)
    a.lt(90)
a.end_fill()
a.up()
a.goto(-250,0)
a.down()
a.pencolor("blue")
a.color("blue")
a.fillcolor("lightblue")
a.begin_fill()
for i in range(3):
    a.fd(220)
    a.lt(120)
a.end_fill()
a.up()
a.goto(0,-250)
a.down()
a.pencolor("yellow")
a.color("yellow")
a.fillcolor("lightblue")
a.begin_fill()
a.circle(100)

a.end_fill()
