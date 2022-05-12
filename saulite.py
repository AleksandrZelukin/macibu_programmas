from turtle import *

color('yellow')
up()
goto(-320,250)
pensize(6)
down()
begin_fill()

for i in range (12):
    forward(200)
    bk(200)
    lt(30)
    i += 1


goto(-320,150)
circle(100)
end_fill()
done()
