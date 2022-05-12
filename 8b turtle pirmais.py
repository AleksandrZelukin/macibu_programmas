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

color("#AA00FF")
penup()
goto(-200,-390)
pendown()
begin_fill()
goto(200,-390)
print(pos())
goto(200,0)
print(pos())
goto(-200,0)
print(pos())
goto(-200,-390)
print(pos())
end_fill()
penup()

goto(0,290)
pendown()
color("dark sea green")
begin_fill()

goto(-250,0)
goto(250,0)
goto(0,290)
end_fill()
