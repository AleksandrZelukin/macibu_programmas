from turtle import *
from random import randint
speed(1000)
krasa = ["red","blue","brown","orange","pink","green","grey"]
numurs = randint(0,6)

def kegelis (x,y):
    for m in range (24):
        num = randint(0,6)
        y += 30
        if m% 2 == 0:
            x = -425            
        else:
            x = -450           
        for k in range(16):
            up()
            setposition(x,y)
            down() 
            color(krasa[num])
            begin_fill()  
            for i in range(2):
                fd(50)
                rt(90)
                fd(25)
                rt(90)
            x += 55  
            end_fill()          
kegelis(-450,-370)
done()