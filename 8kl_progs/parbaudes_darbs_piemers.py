import tkinter as tk
import turtle as tu

logs=tu.Screen()

def kvadrat():
    x = int(tu.textinput("","Norādi X"))
    y = int(tu.textinput("","Norādi Y"))
    z = int(tu.textinput("","Kvadrāta malas garums"))
    tu.up()
    tu.goto(x,y)
    tu.down()
    for i in range(4):
        tu.fd(z)
        tu.lt(90)
    tu.write(f"Kvadrats ar malas garumu {z}px")
    tu.up()
    tu.home()
    
def trijsturis():
    x = int(tu.textinput("Jautājums","Norādi X"))
    y = int(tu.textinput("Jautājums","Norādi Y"))
    tu.up()
    tu.goto(x,y)
    tu.down()
    for i in range(3):
        tu.fd(100)
        tu.lt(120)
    tu.write("Trijsturis")
    tu.up()
    tu.home()   
    
def dzesana():
    tu.clear()   


btn=tk.Button(text='kvadrats',command=kvadrat)
btn.place(x=100,y=100)
btn2=tk.Button(text='trijsturis',command=trijsturis)
btn2.place(x=100,y=150)
btn3=tk.Button(text='zvaigznite')
btn3.place(x=100,y=200)

btn_c=tk.Button(text='Dzest',command=dzesana)
btn_c.place(x=100,y=250)
tu.mainloop()