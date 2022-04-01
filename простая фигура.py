#Простая фигура

from turtle import *
ANGLE = 170
SIZE = 200
pencolor('red')
fillcolor('yellow')
speed(10)
begin_fill()
while True:
    forward(SIZE)
    left(ANGLE)
    if abs(pos()) < 1:
        break
end_fill()


#Знак радиоактивности
#from turtle import *

def square(length):
    for i in range(4):
        forward(length)
        left(90)

def sector(radius, angle):
    forward(radius)
    left(90)
    circle(radius, angle)
    left(90)
    forward(radius)
    left(180-angle)

def move(x, y):
    up()
    forward(x)
    left(90)
    forward(y)
    right(90)
    down()

def radioactive(radius1, radius2, side, angle=60, outlinecol="black", fillcol="yellow"):
    color(outlinecol)
    move(-(side/2), -(side/2))
    
    begin_fill()
    square(side)
    color(fillcol)
    end_fill()
    move((side/2), (side/2))
    color(outlinecol)
    right(90 + angle/2)

    for i in range(3):
        begin_fill()
        sector(radius1,angle)
        left(120)
        color(outlinecol)
        end_fill()

    up()
    forward(radius2)
    left(90)
    down()

    color(fillcol)
    begin_fill()
    circle(radius2)
    color(outlinecol)
    end_fill()

    up()
    left(90)
    forward(radius2)
    width(1)

reset()
width(5)
speed(1)
radioactive(160, 36, 400)

#Оптическая иллюзия
bgcolor("gray60")

pu()
speed(0)
ht()
shape("square")
shapesize(3.2, 3.5)

shift = [10, 0, 10, 28, 10, 0, 10, 28, 10]

tracer(False)
for i in range(9):
    goto(-365 + shift[i], 267-66*i)
    color("black")
    for i in range(11):
        stamp()
        fd(70)
        if pencolor() == "white":
            color("black")
        else:
            color("white")

            
#Гравитация — комета-черепашка вокруг солнца
reset()
color("orange")
dot(10)
center = pos()
color("blue")
shape("turtle")
speed(10)
penup()
goto(200, 0)
pendown()

G = 800
v = Vec2D(0, 1)
t = 0
dt = 1
while t < 1100:
    goto(pos() + v * dt)
    setheading(towards(center))
    r = distance(center)
    acc = (-G / r ** 3) * pos()
    v += acc * dt
    t += dt


mainloop()


