from turtle import *
t = Turtle()
t.screen.setup(800, 800)
def rectangle(x,y,width,height,color):
    t.up()
    t.goto(x,y)
    t.down()
    t.fillcolor("black")
    if (color==1):
     t.fillcolor("red")
    if (color==2):
     t.fillcolor("yellow")   
    if (color==3):
     t.fillcolor("green")
    if (color==4):
     t.fillcolor("blue")
    t.begin_fill()
    t.fd(width)
    t.right(90)
    t.fd(height)
    t.right(90)
    t.fd(width)
    t.right(90)
    t.fd(height)
    t.end_fill()
    t.right(90)
    
rectangle(0,100,200,40,1)
rectangle(30,140,140,40,2)
rectangle(50,180,100,40,3)
rectangle(80,220,40,40,4)


t.screen.exitonclick()
t.screen.mainloop()
