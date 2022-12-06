from tkinter import *
a = Tk()
a.title("mana pirma poga")
a.geometry("200x200")

def pirma():
    label.configure(text="Sveiki, draugs!")
def otra():
    print("Ka iet?")
def close():
   a.destroy()

b1 = Button(text="Pirma poga", background = "blue", foreground="yellow", command = pirma)
b2 = Button(text="Otra poga", background = "red", foreground="yellow", command=otra)
b3 = Button(text="Otra poga", background = "magenta", foreground="yellow", command=close)


b1.pack(expand=True)
label=Label(a)
label.place(x=40, y=50)
b2.pack(expand=True)
b3.pack(expand=True)

a.mainloop()
