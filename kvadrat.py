import turtle

turtle.screensize(canvwidth=800, canvheight=800,bg="black")


def kvadrat(x,y,size):
    turtle.pu()
    turtle.goto(-x,y)
    turtle.pd()
    turtle.pensize(4)
    turtle.colormode(255)
    turtle.color(255,0,0)
    turtle.fillcolor(0,255,0)
    turtle.begin_fill()
    turtle.shape("turtle")
    for i in range (4):
        turtle.fd(size)
        turtle.lt(90)
    turtle.end_fill()


def triangle(x,y,size):
    turtle.pu()
    turtle.goto(-x,y)
    turtle.pd()
    turtle.pensize(4)
    turtle.colormode(255)
    turtle.color(255,0,0)
    turtle.fillcolor(255,0,0)
    turtle.begin_fill()
    turtle.shape("turtle")
    for i in range (3):
        turtle.fd(size)
        turtle.lt(120)
    turtle.end_fill()

def sesturis(x,y,size):
    turtle.pu()
    turtle.goto(-x,y)
    turtle.pd()
    turtle.pensize(4)
    turtle.colormode(1)
    turtle.color(1,0,0)
    turtle.fillcolor(0,0,1)
    turtle.begin_fill()
    turtle.shape("turtle")
    for i in range (6):
        turtle.fd(size)
        turtle.lt(60)
    turtle.end_fill()



kvadrat(-100,-200,150)
triangle(100,100,100)
sesturis(150,-150,80)


