import tkinter
import turtle

logs=turtle.Screen()
logs.bgcolor("lightblue")
logs.setup(600,600)
#canva=logs.getcanvas()


krasa=['red', 'green','blue','black']

def kvadrat():
    turtle.clear()
    turtle.pu()
    turtle.goto(-50,-50)
    turtle.pd()
    turtle.pensize(4)
    turtle.begin_fill()
    turtle.shape("turtle")
    for i in range (4):
        turtle.color(krasa[0])
        turtle.fillcolor(krasa[1])
        turtle.fd(100)
        turtle.lt(90)
    turtle.end_fill()

def oktaedr():
    turtle.clear()
    turtle.pu()
    turtle.goto(-50,-50)
    turtle.pd()
    turtle.pensize(4)
    turtle.begin_fill()
    turtle.shape("turtle")
    for i in range (8):
        turtle.color(krasa[2])
        turtle.fillcolor(krasa[1])
        turtle.fd(100)
        turtle.lt(45)
    turtle.end_fill()

def sesturis():
    turtle.clear()
    turtle.pu()
    turtle.goto(-50,-50)
    turtle.pd()
    turtle.pensize(4)
    turtle.begin_fill()
    turtle.shape("turtle")
    for i in range (6):
        turtle.color(krasa[1])
        turtle.fillcolor(krasa[2])
        turtle.fd(100)
        turtle.lt(60)
    turtle.end_fill()

def triangle():
    turtle.clear()
    turtle.pu()
    turtle.goto(-50,-50)
    turtle.pd()
    turtle.pensize(4)
    turtle.begin_fill()
    turtle.shape("turtle")
    for i in range (3):
        turtle.color(krasa[1])
        turtle.fillcolor(krasa[2])
        turtle.fd(100)
        turtle.lt(120)
    turtle.end_fill()

def clear_all():
    turtle.clear()


btn4=tkinter.Button(text='kvadrat', command=kvadrat)
#btn4.pack()
btn4.place(x=10,y=20)

btn8=tkinter.Button(text='oktaedr', command=oktaedr)
#btn8.pack()
btn8.place(x=10,y=50)

btn6=tkinter.Button(text='sesturis', command=sesturis)
#btn6.pack()
btn6.place(x=10,y=80)

btn3=tkinter.Button(text='tissturis', command=triangle)
#btn3.pack()
btn3.place(x=10,y=120)

btn_clear=tkinter.Button(text="clear All", command=clear_all)
btn_clear.place(x=10, y=150)


#turtle.mainloop()
turtle.exitonclick()
