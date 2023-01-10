from tkinter import *

a = Tk()
a.title("Manas pogas")
a.geometry("300x150")


entry = Entry(font="32")
entry.pack()

label = Label(font="32")
label.pack()

def display():
    label["text"] = entry.get()

def clear():
    entry.delete(0, END)
    
btn1 = Button(a, text="ievads", command=display)
btn2 = Button(a, text="notirit", command=clear)
btn1.place(relx=.2, rely=.4)
btn2.place(relx=.6, rely=.4)

a.mainloop()

