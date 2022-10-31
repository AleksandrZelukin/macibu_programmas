from cgitb import text
from tkinter import *

a=Tk()

a.title("Skolotāja poga")
a.geometry("800x800")

text = Text(width=20, height=1, bg="lightblue")
text.pack(ipadx=100, ipady=5)

text = Entry(width=20, bg="yellow")
text.pack(ipadx=100, ipady=5)

label = Label()
label.place(relx=0.5, rely=0.1)

label1=Label(text="")
label1.place(relx=0.3, rely=0.2)

label2=Label(text="")
label2.place(relx=0.3, rely=0.3)

label3=Label(text="")
label3.place(relx=0.3, rely=0.4)

def A():
    label1.config(text="Ka tev sauc?")

def B():
    label2.config(text="Kur tu dzivo?")

def C():
    label3.config(text="Cik tev gadi?")


def quit():
     a.destroy()

btn1 = Button(text="Poga 1",background="red",foreground="blue",padx="20",pady="1",font="16", command=A)

btn1.place(x=100, y=100)


btn2 = Button(text="Poga 2",background="lightgreen",foreground="blue",padx="20",pady="1",font="16", command=B)

btn2.place(x=100, y=150)


btn3 = Button(text="Poga 3",background="yellow",foreground="blue",padx="20",pady="1",font="16", command=C)

btn3.place(x=100, y=200)


btn4 = Button(text="Beigt",background="yellow",foreground="blue",padx="20",pady="1",font="16", command=quit)

btn4.place(x=100, y=250)



a.mainloop()
