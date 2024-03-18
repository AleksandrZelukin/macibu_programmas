import tkinter as tk
import turtle as tu

logs=tu.Screen()

def kvadrat():
    tu.clear()
    for i in range(4):
        tu.fd(100)
        tu.lt(90)
        
def trijsturis():
    tu.clear()
    for i in range(3):
        tu.fd(100)
        tu.lt(120)
        
def tirit():
    tu.clear()

btn=tk.Button(text='kvadrats',command=kvadrat)
btn.place(x=100,y=100)
btn2=tk.Button(text='trijsturis',command=trijsturis)
btn2.place(x=100,y=150)


btn_c=tk.Button(text='Dzest',command=tirit)
btn_c.place(x=100,y=250)
tu.mainloop()