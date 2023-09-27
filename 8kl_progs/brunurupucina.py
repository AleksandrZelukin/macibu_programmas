from turtle import *

screensize(canvwidth=200, canvheight=150,bg="yellow")

pencolor("red")
fillcolor("yellow")
up()
goto(-50,-50)
pensize(5)
a = int(input("Cik malus tev vajag? "))
down()
begin_fill()
for i in range(a):
    forward(100-2*a)
    left(360/a)
end_fill()
done()