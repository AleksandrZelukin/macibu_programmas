import tkinter as tk
import turtle as tu

logs=tu.Screen()

def kvadrat():
    for i in range(4):
        tu.fd(100)
        tu.lt(90)

btn=tk.Button(text='kvadrats',command=kvadrat)
btn.place(x=100,y=100)

tu.mainloop()