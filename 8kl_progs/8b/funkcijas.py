from turtle import *

def kvadrat():
    for i in range(4):
        fd(100)
        lt(90)

def triangle():
    for i in range(3):
        fd(100)
        lt(120)
        
triangle()

goto(100,-100)
kvadrat()

goto(-100,100)
triangle()       

mainloop()