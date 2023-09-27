from turtle import *
a=int(input())
up()
goto(-100,-100)
pensize(5)
pencolor("red")
fillcolor("yellow")
down()
begin_fill()
for i in range(a):
    forward(100-2*a)
    left(360/a)
end_fill()
done()