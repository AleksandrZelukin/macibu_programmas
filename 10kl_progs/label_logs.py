from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('400x400+800+300')
root.title('Mans pirmais logs')

def start():
    name = atbilde.get()
    #messagebox.showinfo('Sveiki!', '{name}'.format(name=name))
    messagebox.showinfo('Sveiki',name)

info = Label(root,text="Sveiki, draugs!")
info.pack()

jautajums = Label(root, text="Ka tevi sauc?")
jautajums.pack(padx=10, pady=10)

atbilde = Entry(root)
atbilde.pack()

btn = Button(root, text='nospiež mani', command=start)
btn.pack(padx=10, pady=10)
btn2 = Button(root, text='Iziet no progrāmmas', command=root.destroy )
btn2.pack()

root.mainloop()