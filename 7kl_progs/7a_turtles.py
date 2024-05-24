from turtle import *

t = Turtle()
t.pensize(6)
t.shapesize(2)
t.pencolor("red")
t.shape("turtle")
t.color("green")

for i in range(4):
    t.fd(100)
    t.lt(90)
t.up()
t.goto(-250,-300)
t.down()
t.pencolor("blue")
for i in range(3):
    t.fd(100)
    t.lt(120)

t.up()
t.goto(-200,250)
t.down()
t.pencolor("yellow")
t.circle(50)
