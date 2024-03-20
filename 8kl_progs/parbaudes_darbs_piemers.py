import tkinter as tk
import turtle as tu

logs=tu.Screen()

def kvadrat():
    x = tu.textinput("","")
    y = tu.textinput("","")
    tu.up()
    tu.goto(x,y)
    tu.down()
    for i in range(4):
        tu.fd(100)
        tu.lt(90)
    tu.write(f"Kvadrats ar malas garumu 100px")
    tu.up()
    tu.home()
    
    
def dzesana():
    tu.clear()   


btn=tk.Button(text='kvadrats',command=kvadrat)
btn.place(x=100,y=100)
btn2=tk.Button(text='trijsturis')
btn2.place(x=100,y=150)
btn3=tk.Button(text='zvaigznite')
btn3.place(x=100,y=200)

btn_c=tk.Button(text='Dzest')
btn_c.place(x=100,y=250)
tu.mainloop()