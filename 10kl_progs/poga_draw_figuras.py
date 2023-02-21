import tkinter as tk
import turtle as tu
import random

logs = tu.Screen()
logs.setup(800,600)
tu.pensize(4)
tu.shape('turtle')
tu.speed(1000)
krasa = ['red','pink','yellow','blue','green','orange']

def kvadrat():
    tu.clear()
    tu.up()
    tu.goto(-50,-50)
    tu.down()
    random.shuffle(krasa)
    tu.color(krasa[0])
    for i in range(4):
        tu.fillcolor(krasa[1])
        tu.fd(100)
        tu.lt(90)
        tu.end_fill()

def trijsturis():
    tu.clear()
    tu.up()
    tu.goto(-50,-50)
    tu.down()
    random.shuffle(krasa)
    tu.color(krasa[0])
    for i in range(3):
        tu.fd(100)
        tu.lt(120)

def notirit():
    tu.clear()

btn_kvadrat=tk.Button(text="Kvadrats",command=kvadrat)
btn_trijstur=tk.Button(text="Trijsturis",command=trijsturis)
btn_clear=tk.Button(text="Notirit viss",command=notirit)
btn_kvadrat.place(x=20,y=100)
btn_trijstur.place(x=20,y=140)
btn_clear.place(x=20,y=180)

tu.mainloop()