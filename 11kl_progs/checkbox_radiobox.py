import tkinter as tk 

logs = tk.Tk()
logs.title("checkbox")
logs.geometry("300x300")

def izvele():
    if (var2.get()== 1) and (var4.get() == 1):
        atbilde.config(text="Pareizā atbilde!")
    if (var2.get()== 1) and (var4.get() == 1) and (var3.get() == 1):
        atbilde.config(text="Nepareizā atbilde!")
    if (var2.get()== 1) and (var4.get() == 1) and (var3.get() == 1) and (var2.get() == 1):
        atbilde.config(text="Nepareizā atbilde!")

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
c1 = tk.Checkbutton(text="1.variants",variable=var1,onvalue=1,offvalue=0,command=izvele)
c1.pack()
c2 = tk.Checkbutton(text="2.variants",variable=var2,onvalue=1,offvalue=0,command=izvele)
c2.pack()
c3 = tk.Checkbutton(text="3.variants",variable=var3,onvalue=1,offvalue=0,command=izvele)
c3.pack()
c4 = tk.Checkbutton(text="4.variants",variable=var4,onvalue=1,offvalue=0,command=izvele)
c4.pack()
atbilde = tk.Label()
atbilde.pack()

def izvele1():
    atbilde1.config(text='Tu izvēlē variants ' + var.get())


var = tk.StringVar()
r1 = tk.Radiobutton(text='Variants A', variable=var, value='A', command=izvele1)
r1.pack()
r2 = tk.Radiobutton(text='Variants B', variable=var, value='B', command=izvele1)
r2.pack()
r3 = tk.Radiobutton(text='Variants C', variable=var, value='C', command=izvele1)
r3.pack()
atbilde1 = tk.Label()
atbilde1.pack()
logs.mainloop()