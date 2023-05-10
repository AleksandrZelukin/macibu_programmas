from turtle import *

def kvadrats():
    up()
    goto(x,y)
    down()
    for i in range(4):
        fd(a)
        lt(90)

x=int(textinput('koordinates', 'X'))
y=int(textinput('koordinates', 'Y'))
a=int(textinput('Malu izmers', 'cik?'))

kvadrats()
x=int(textinput('koordinates', 'X'))
y=int(textinput('koordinates', 'Y'))
kvadrats()
mainloop()