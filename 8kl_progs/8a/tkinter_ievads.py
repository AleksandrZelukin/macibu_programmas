# fom text.py
from tkinter import *
logs = Tk()
logs.geometry("500x300+600+150")
logs.title('Mana pirma programma') 

def get_text():
    label2['text'] = text.get()

def remove_text():
    label2.config(text="")
 
def iziet():
    logs.destroy()

label1=Label(text='uzraksti savu vārdu')
label1.grid(row=0,column=0)

text = Entry()
text.grid(row=0,column=1)

btn1=Button(text="Paņemt",command=get_text)
btn1.grid(row=0,column=2)

btn2=Button(text="Beigt",command=iziet)
btn2.grid(row=2,column=1)

btn3=Button(text="Dzest",command=remove_text)
btn3.grid(row=1,column=1)

label2= Label()
label2.grid(row=1,column=0)

 
logs.mainloop()
