import tkinter
import turtle

logs=turtle.Screen()
# logs.setup(800,800)
logs=tkinter.Tk()

def kvadrats():
    turtle.clear()
    for i in range(4):
        turtle.fd(100)
        turtle.lt(90)
    
def ovals():
    turtle.clear()
    turtle.goto(0,0)
    turtle.circle(100)

def iziet():
    logs.destroy()

btn1=tkinter.Button(text='kvadrats',command=kvadrats)
btn1.place(x=10,y=80)
btn2=tkinter.Button(text='riņķis',command=ovals)
btn2.place(x=10,y=180)
btn3=tkinter.Button(text='iziet')
btn3.place(x=10,y=280)
turtle.mainloop()