from tkinter import *
from tkinter import messagebox
logs = Tk()

logs.geometry('600x600+800+200')

def izeja():
    logs.destroy()
    
data = StringVar()

def vards():
    label3.config(data.get()) 
    
    
label1 = Label(text='Hello world!')
label1.pack()

label2 = Label(text='Hello Me!')
label2.pack()

entry1 = Entry(textvariable=data)
entry1.pack()  

btn1 = Button(text='Press Me!',command=vards) 
btn1.pack()  

label3 = Label()
label3.pack()

btn2 = Button(text='iziet',fg='yellow',bg='red',command=izeja)
btn2.pack()

logs.mainloop()