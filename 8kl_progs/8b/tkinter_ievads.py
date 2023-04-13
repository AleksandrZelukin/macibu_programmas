from tkinter import *
from tkinter import messagebox
logs = Tk()

logs.geometry('600x600+800+200')

def vards():
    a=entry1.get()
    label3.configure(a)

def izeja():
    logs.destroy()
    

def welcomeMessage():
    name = entry1.get()
    return messagebox.showinfo('message',f'Sveiki! {name}, Laipni ludzam 92.vidusskolā.')    

label1 = Label(text='Hello world!',font=('Arial',32),bg='red')
label2 = Label(text='Hello Me!',font=("Times", "24", "bold italic"),fg='blue')
entry1 = Entry(font=('Arial',32))
label3 = Label(text='aaa',font=("Times", "24", "bold italic"),fg='blue')
btn1 = Button(text='Press Me!',font=('Arial',32),fg='yellow',bg='blue',command=welcomeMessage)

btn2 = Button(text='iziet',font=('Arial',32),fg='yellow',bg='red',command=izeja)



label1.pack()
label2.pack()
entry1.pack()
btn1.pack()
label3.pack()
btn2.place(x=270,y=400)
logs.mainloop()