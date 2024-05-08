from turtle import *
from random import randint
speed(1000)
krasa = ['red', 'yellow', 'green', 'blue', 'purple', 'black', 'orange', 'pink'] 
col = randint(0,7)
col1 = krasa[col]
def kvadrat(x,y):
    up()
    goto(x,y)
    col = randint(0,7)
    col1 = krasa[col]
    color(col1)
    down()
    for i in range(4):
        fd(100)
        lt(90)
        
        
onscreenclick(kvadrat)   
done()