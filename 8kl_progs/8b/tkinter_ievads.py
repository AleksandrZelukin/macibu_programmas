from tkinter import *

logs = Tk()

logs.geometry('1000x400+800+200')

def izeja():
    logs.destroy()
    
# data = StringVar()

# def vards():
#     label3.config(data.get()) 
    
def vards():
    label3["text"] = entry1.get()


    
label1 = Label(text='Sveiki!',font=('Arial','24'))
label1.grid(row=0,column=0)

label2 = Label(text='Kur tu dzivo?',font=('Arial','24'))
label2.grid(row=0,column=1)

# entry1 = Entry(textvariable=data,font=('Arial','24'))
entry1 = Entry(font=('Arial','24'))
entry1.grid(row=0,column=2)

btn1 = Button(text='Saglabāt',command=vards,font=('Arial','24')) 
btn1.grid(row=0,column=3)

label3 = Label(font=('Arial','24'))
label3.grid(row=1,column=1)

btn2 = Button(text='iziet',fg='yellow',bg='red',command=izeja,font=('Arial','24'))
btn2.grid(row=2,column=1)

logs.mainloop()