import turtle
#from turtle import *
a = turtle.Turtle()
a.shape("turtle")
#a.screen.setup(800, 800)
def kvadrats(x,y, color, pen):
    a.up()
    a.pensize(pen)
    a.goto(-x, y)
    a.down()
    a.fillcolor(color)
    a.begin_fill()
    a.goto(x, y)
    a.goto(x, - y)
    a.goto(-x,-y)
    a.goto(-x, y)
    a.end_fill()



kvadrats(200,200, "red",5)
kvadrats(150,150, "blue",4)
kvadrats(100,100,"yellow",3)
kvadrats(50,50,"brown",2)
kvadrats(25,25,"green",1)


turtle.exitonclick()
#turtle.mainloop()
