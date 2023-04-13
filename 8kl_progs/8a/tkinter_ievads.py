# fom text.py
from tkinter import *
logs = Tk()
logs.geometry("400x400")
 

 
def get_text():
    label['text'] = text.get()
 
def iziet():
    logs.destroy()

 
text = Entry()
text.grid(row=0,column=0)

btn1=Button(text="Paņemiet",command=get_text)
btn1.grid(row=0,column=1)

btn2=Button(text="Beigt",command=iziet)
btn2.grid(row=1,column=1)

label = Label()
label.grid(row=2,column=0)

 
logs.mainloop()
