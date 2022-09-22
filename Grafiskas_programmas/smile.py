from turtle import *
speed(10)
def smile (x,y): 
    pensize(4)
    ht()
    pencolor("darkred")
    fillcolor("yellow")
    up()
    setpos(x,y)
    begin_fill()
    down()
    circle(100) #Seja
    end_fill()
    
    up()
    setpos (-70+x,80+y)
    setheading(-60)
    down()
    color("red")
    pensize(10)
    circle(80,120,6) #smile
    
    up()
    setpos(-50+x,120+y)
    down()
    dot(20) #acs
    
    up()
    #setpos(50+x,120+y)
    setx(50+x)
    down()
    dot(20)#acs
    up()
    home()

smile(100,200)
smile(100,-200)
smile(-100,160)
smile(-180,-20)

exitonclick()
