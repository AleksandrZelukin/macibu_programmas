from tkinter import *

logs = Tk()

logs.geometry('600x400+800+200')

def izeja():
    logs.destroy()
    
# data = StringVar()

# def vards():
#     label3.config(data.get()) 
    
def vards():
    label3["text"] = entry1.get()

def vards2():
    label3["text"] = text1.get(1.0,END)

    
label1 = Label(text='Sveiki!')
label1.grid(row=0,column=0)

label2 = Label(text='Kur tu dzivo?')
label2.grid(row=0,column=1)

# entry1 = Entry(textvariable=data,font=('Arial','24'))
entry1 = Entry()
entry1.grid(row=0,column=2)

btn1 = Button(text='Saglabāt',command=vards) 
btn1.grid(row=0,column=3)

text1 = Text(width=20, height=2)
text1.grid(row=0,column=4)

btn2 = Button(text='Saglabāt',command=vards2) 
btn2.grid(row=0,column=5)
r1 = Checkbutton(text='Jā')
r1.grid(row=1,column=0)
r2 = Checkbutton(text='Nē')
r2.grid(row=1,column=1)

label3 = Label()
label3.grid(row=1,column=3)

btn2 = Button(text='iziet',fg='yellow',bg='red',command=izeja)
btn2.grid(row=8,column=3)
w2 = Scale(logs, from_=0, to=200, length=600,tickinterval=10, orient=HORIZONTAL)
w2.grid(row=7,column=0, columnspan=6)
logs.mainloop()