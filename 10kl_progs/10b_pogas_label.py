import tkinter as tk

a = tk.Tk()

a.geometry("300x300")



entry = tk.Entry(a, width=5, font=("size 32"))
entry.pack()


label = tk.Label(text = "Sveiki, draugs!", font=("size 32"))
label.pack()

def clear():
    label.config(text="Sveiki, draugs!")
    
def ievads():
    label["text"] = entry.get()

btn1 = tk.Button(a, text="ievads", command=ievads)
btn1.pack()

btn2 = tk.Button(a, text="notirit", command=clear)
btn2.pack()

a.mainloop()