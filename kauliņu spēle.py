from tkinter import *
from random import randint

logs = Tk()

logs.title("Kauliņu spēle")
logs.geometry("400x160")
teksts = Text(width=10, height=4, bg="lightblue",fg='red')

def ripinat ():
    teksts.delete(0.0, END)
    teksts.insert(END, str(randint(1,6)))
    teksts.tag_add("spele", 0.0, "end")
    teksts.tag_config("spele", justify=CENTER, font=("Arial", 48, "bold"))


pogaA = Button(logs, text='Klikšņi, lai ripinātu!',
               bg="red", fg="blue", command=ripinat)
pogaB = Button(logs, text="Iziet", bg="red", command=logs.destroy)

teksts.pack()

pogaA.pack(pady=20)
pogaB.pack(pady=1)

logs.mainloop()