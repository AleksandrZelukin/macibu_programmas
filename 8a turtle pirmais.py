from turtle import *

color('yellow')
up()
goto(-350,250)
down()
pensize(6)
begin_fill()
for i in range (12):
    fd(200)
    bk(200)
    lt(30)
    i+=1

goto(-350, 150)
circle(100)
end_fill()











done()
