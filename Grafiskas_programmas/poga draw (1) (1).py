import tkinter
import turtle

logs=turtle.Screen()
logs.setup(1200,800)
#can=logs.getcanvas()

col = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

def up_draw():
    turtle.fd(10)

def fig1():
    turtle.clear()
    turtle.pu()
    turtle.goto(-50,-50)
    turtle.pd()
    turtle.pensize(4)
    turtle.begin_fill()
    turtle.shape("turtle")
    for i in range (4):
        turtle.color(col[2])
        turtle.fillcolor(col[1])
        turtle.fd(100)
        turtle.lt(90)
    turtle.end_fill()
def fig2():
    turtle.clear()   

btn_up=tkinter.Button(text="kvadrat",command=fig1)
btn_clear=tkinter.Button(text="attirit viss",command=fig2)
#can.create_window(-300, -100, window=btn_up)
btn_up.place(x=10,y=80)
btn_clear.place(x=10,y=120)


turtle.mainloop()
