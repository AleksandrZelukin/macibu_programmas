from turtle import *
from random import randrange
a = int(input("Cik malu tev vajag? "))
krasa=("red","blue","yellow","green","orange")
up()
goto(-10,-10)
pensize(4)
k = randrange(0,4)
l = randrange(1,3)
pencolor(krasa[k])
fillcolor(krasa[l])
down()
begin_fill()
for i in range(a):
    fd(100-2*a)
    lt(360/a)
end_fill()
done()