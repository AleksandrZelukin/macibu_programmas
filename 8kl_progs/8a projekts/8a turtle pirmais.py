from turtle import *
setup(1200,1024)

color('yellow')
up()
goto(-350,250)
down()
pensize(6)
begin_fill()
for i in range (12):
    fd(200)
    bk(200)
    lt(15)
    fd(400)
    bk(400)
    lt(15)
    i+=2
goto(-350, 150)
circle(100)
end_fill()

up()
goto(-200,-100)
down()
color("darkred")
begin_fill()
goto(-200,-400)
goto(200,-400)
goto(200,-100)
goto(-200,-100)
end_fill()


up()
goto(0,100)
down()
color("#AA00FF")
begin_fill()
goto(-250,-100)
goto(250,-100)
goto(0,100)
end_fill()







done()
