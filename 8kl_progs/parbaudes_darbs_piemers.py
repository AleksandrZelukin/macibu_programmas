import tkinter as tk
import turtle as tu

logs=tu.Screen()

def kvadrat():
    vietax = tu.textinput("Jautājums","Norādi X")
    vietay = tu.textinput("Jautājums","Norādi Y")
    tu.up()
    tu.goto(int(vietax),int(vietay))
    tu.down()
    for i in range(4):
        tu.fd(100)
        tu.lt(90)
    tu.write("Kvadrats")
    tu.up()
    tu.home()   
def trijsturis():
    vietax = tu.textinput("Jautājums","Norādi X")
    vietay = tu.textinput("Jautājums","Norādi Y")
    tu.goto(int(vietax),int(vietay))
    tu.up()
    tu.goto(int(vietax),int(vietay))
    tu.down()
    for i in range(3):
        tu.fd(100)
        tu.lt(120)
    tu.write("Trijsturis")
    tu.up()
    tu.home()

def zvaigznite():
    vietax = tu.textinput("Jautājums","Norādi X")
    vietay = tu.textinput("Jautājums","Norādi Y")
    tu.goto(int(vietax),int(vietay))
    tu.up()
    tu.goto(int(vietax),int(vietay))
    tu.down()
    tu.lt(36)
    for i in range(5):
        tu.fd(100)
        tu.lt(144)
    tu.write("Zvaigznite")
    tu.up()
    tu.home()      
def tirit():
    tu.clear()

btn=tk.Button(text='kvadrats',command=kvadrat)
btn.place(x=100,y=100)
btn2=tk.Button(text='trijsturis',command=trijsturis)
btn2.place(x=100,y=150)
btn3=tk.Button(text='zvaigznite',command=zvaigznite)
btn3.place(x=100,y=200)

btn_c=tk.Button(text='Dzest',command=tirit)
btn_c.place(x=100,y=250)
tu.mainloop()