from turtle import *
def geo():
    i = textinput('Ievads','Figuras veids')
    a=int(textinput('Ievads','malu garums'))  
    if i =="kvadrats":
        for i in range(4):
            fd(a)
            lt(90)
    if i =="trijstūris" or i=='triangle':
        for i in range(3):
            fd(a)
            lt(120)
  

geo()
mainloop()