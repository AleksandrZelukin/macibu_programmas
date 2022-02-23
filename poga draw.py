import tkinter as tk
import turtle as tu

logs=tu.Screen()
logs.setup(800,800)
can=logs.getcanvas()


def up_draw():
    tu.fd(10)

btn_up=tk.Button(text="up",command=up_draw)

can.create_window(-300, -100, window=btn_up)
#btn_up.pack()


tu.mainloop()
