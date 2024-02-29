import turtle as tu
import tkinter as tk

logs = tu.Turtle()

def kvadrats():
    tu.clear()
    for i in range(4):
        tu.fd(200)
        tu.lt(90)
def trijsturis():
    tu.clear()
    for i in range(3):
        tu.fd(200)
        tu.lt(120)
def sesturis():
    tu.clear()
    for i in range(6):
        tu.fd(120)
        tu.lt(60)
def notirit():
    tu.clear()
poga1 = tk.Button(text="kvadrats",command=kvadrats)
poga1.place(x=50,y=50)
poga2 = tk.Button(text="trijsturis",command=trijsturis)
poga2.place(x=50,y=80)
poga3 = tk.Button(text="sešsturis",command=sesturis)
poga3.place(x=50,y=110)
poga4 = tk.Button(text="notirit visu",bg = "red",fg="yellow" ,command=notirit)
poga4.place(x=50,y=140)
