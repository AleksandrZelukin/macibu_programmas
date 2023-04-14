from tkinter import *
win = Tk()
win.geometry('800x800+700+150')

data = StringVar()

def izeja():
    win.destroy()


def vards():
    label2 = entry1.get()

label1 = Label(text='Jusu vārds',font=('Arial','24'),bg='green',fg='blue').pack()

entry1 = Entry(textvariable=data).pack()

btn1 = Button(text='Press me!',font=('Arial','24'),bg='red',fg='yellow',command=vards).pack()

label2 = Label(font=('Arial','24'),fg='blue').pack()

btn2 = Button(text="Izeja",font=('Arial','24'),bg='red',fg='yellow',command=izeja).pack()


win.mainloop()