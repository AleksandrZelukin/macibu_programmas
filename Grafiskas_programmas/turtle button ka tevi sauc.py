import turtle
import tkinter

def show_Ivars():
    turtle.ht()
    turtle.penup()
    turtle.goto (15, 300)
    turtle.color("black")
    turtle.write("Ivars", move=True, align="center", font=("Times New Roman", 40, "bold"))

def show_Riga():
    turtle.ht()
    turtle.penup()
    turtle.goto (15, 200)
    turtle.color("black")
    turtle.write("Rīgā", move=False, align="center", font=("Times New Roman", 40, "bold"))





screen = turtle.Screen()
screen.setup(800,800)

can = screen.getcanvas()

btn1 = tkinter.Button(can.master, text="Kā tevi sauc?", command=show_Ivars)
can.create_window(-300, -300, window=btn1)

btn2 = tkinter.Button(can.master, text="Kur tu dzīvo?", command=show_Riga)
can.create_window(-300, -200, window=btn2)

turtle.mainloop()
