from turtle import *
t = Turtle()
t.screen.setup(500, 500)
def triangle(x1,y1,x2,y2,x3,y3,color):
    t.up()
    t.goto(x1,y1)
    t.down()
    t.fillcolor("black")
    if (color==1):
     t.fillcolor("red")
    if (color==2):
     t.fillcolor("yellow")   
    if (color==3):
     t.fillcolor("green")
    t.begin_fill()
    t.goto(x2,y2)
    t.goto(x3,y3)
    t.goto(x1,y1)
    t.end_fill()
triangle(10,80,50,130,100,80,1)    
triangle(10,30,50,80,100,30,2)
triangle(10,-20,50,30,100,-20,3)

t.screen.exitonclick()
t.screen.mainloop()
