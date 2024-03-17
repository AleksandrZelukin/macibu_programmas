from turtle import *
def kvadrats():
    up()
    goto(x,y)  
    down()     
    for i in range(4):
        fd(100)
        lt(90)

x=int(textinput('koordināte X',''))  
y=int(textinput('koordināte Y',''))       
 
kvadrats()
x=int(textinput('koordināte X',''))  
y=int(textinput('koordināte Y',''))       
 
kvadrats()
x=int(textinput('koordināte X',''))  
y=int(textinput('koordināte Y',''))       
 
kvadrats()
mainloop()