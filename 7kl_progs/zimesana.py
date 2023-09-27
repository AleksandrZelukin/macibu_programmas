from turtle import *
speed(100)
pensize(6)
pencolor('red')
fillcolor('yellow')
penup()
goto(0,0)
pendown()
begin_fill()
for i in range (4):
    forward(100)
    left(90)
end_fill()
penup()    
backward(150)

pendown()

fillcolor('brown')
begin_fill()
for i in range (3):
    forward(100)
    left(120)
end_fill()

penup()
goto(-40,-50)
pendown()
fillcolor('lightblue')
begin_fill()
for i in range (6):
    forward(80)
    left(-60)
end_fill()
done()
