from tkinter import *

a=Tk()

a.title("Skolotāja poga")
a.geometry("800x800")

def A():
    print("Ka tev sauc?")

def B():
    print ("Kur tu dzivo?")


def quit():
     a.destroy()

btn1 = Button(text="Poga 1",background="red",foreground="blue",padx="20",pady="1",font="16", command=A)

btn1.place(x=100, y=100)


btn2 = Button(text="Poga 2",background="lightgreen",foreground="blue",padx="20",pady="1",font="16", command=B)

btn2.place(x=100, y=150)


btn3 = Button(text="Poga 3",background="yellow",foreground="blue",padx="20",pady="1",font="16", command=A)

btn3.place(x=100, y=200)


btn4 = Button(text="Beigt",background="yellow",foreground="blue",padx="20",pady="1",font="16", command=quit)

btn4.place(x=100, y=250)



a.mainloop()
