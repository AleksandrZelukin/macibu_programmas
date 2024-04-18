from turtle import *

up()
setposition(-100,-300)
down()
fillcolor("lightblue")
begin_fill()
for i in range(4):
    fd(200)
    lt(90)
    
up()
setposition(-150,-100)
down()

for i in range(3):
    fd(300)
    lt(120)
end_fill()
up()
setposition(-200,200)
down() 
pencolor("yellow")
fillcolor("yellow") 
pensize(6) 
for i in range(8):
    fd(100)
    bk(100)
    lt(45)
setposition(-200,160)    
begin_fill()
circle(40,180)
end_fill()
done()