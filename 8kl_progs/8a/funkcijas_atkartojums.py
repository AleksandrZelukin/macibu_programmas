from turtle import *

def kvadrats():
    x=int(textinput('koordinates', 'X'))
    y=int(textinput('koordinates', 'Y'))
    a=int(textinput('Malu izmers', 'cik?'))
    up()
    goto(x,y)
    down()
    for i in range(4):
        fd(a)
        lt(90)



kvadrats()
kvadrats()
mainloop()