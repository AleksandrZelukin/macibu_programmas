# from tkinter import *

# root = Tk()
# btn1 = Button(root, text="One", bg="red", fg="white")
# btn2 = Button(root, text="Two", bg="green", fg="black")
# btn3 = Button(root, text="Three", bg="blue", fg="yellow")
# btn4 = Button(root, text="Four", bg="purple", fg="lightblue")
# btn5 = Button(root, text="Five", bg="blue", fg="pink")
# btn1.pack()
# btn2.pack(side=TOP)
# btn3.pack(side=LEFT)
# btn4.pack(side=RIGHT)
# btn5.pack(side=BOTTOM)
# root.mainloop()

# from tkinter import *

# root = Tk()
# root.title("Welcome to the second entry app")
# lbl_login = Label(root, text="Login")
# lbl_pass = Label(root, text="Password")
# txt1 = Entry(root, width=10)
# txt2 = Entry(root, width=10)
# btn = Button(root, text="Enter")
# lbl_login.grid(row=0, sticky=E)
# lbl_pass.grid(row=1, sticky=E)
# txt1.grid(row=0, column=1)
# txt2.grid(row=1, column=1)
# btn.grid(columnspan=2, sticky=NSEW)
# root.mainloop()

# from tkinter import *
# from tkinter.filedialog import *

# root = Tk()
# op = askopenfilename()
# sa = asksaveasfilename()

# root.mainloop()

from tkinter import *
from tkinter import messagebox


def clear():
    name_entry.delete(0, END)
    surname_entry.delete(0, END)


def display():
    messagebox.showinfo("GUI Python", name_entry.get() + " " + surname_entry.get())

root = Tk()
root.title("GUI на Python")

name_label = Label(text="Vārds:")
surname_label = Label(text="Uzvārds:")

name_label.grid(row=0, column=0, sticky="w")
surname_label.grid(row=1, column=0, sticky="w")

name_entry = Entry()
surname_entry = Entry()

name_entry.grid(row=0,column=1, padx=5, pady=5)
surname_entry.grid(row=1,column=1, padx=5, pady=5)


name_entry.insert(0, "Aigars")
surname_entry.insert(0, "Berziņš")

display_button = Button(text="Display", command=display)
clear_button = Button(text="Clear", command=clear)

display_button.grid(row=2, column=0, padx=5, pady=5, sticky="e")
clear_button.grid(row=2, column=1, padx=5, pady=5, sticky="e")

root.mainloop()