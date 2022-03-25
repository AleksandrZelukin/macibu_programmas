import turtle
import tkinter as tk

def show_cat():
    turtle.ht()
    turtle.penup()
    turtle.goto (15, 220)
    turtle.color("black")
    turtle.write("CAT", move=False, align="center", font=("Times New Roman", 120, "bold"))

screen = turtle.Screen()
screen.setup(800,800)

canvas = screen.getcanvas()

button = tk.Button(canvas.master, text="Click Me", command=show_cat)
canvas.create_window(0, 200, window=button)

turtle.mainloop()
