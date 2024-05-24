from turtle import *
from random import randint
krasa = ["red","blue","green","orange","yellow","indigo","purple"]
#https://cs111.wellesley.edu/labs/lab02/colors
num = randint(0,6)
fillcolor(krasa[num])
begin_fill()
for i in range(4):
    fd(100)
    lt(90)
end_fill()
up()
goto(-200,0)
down()
fillcolor(krasa[4])
begin_fill()
for i in range(3):
    fd(100)
    lt(120)
end_fill()
up()
goto(0,-200)
down()
fillcolor(krasa[3])
begin_fill()
circle(50)
end_fill()
