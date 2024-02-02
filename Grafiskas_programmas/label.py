from tkinter import *
 
root = Tk()
root.title("GUI на Python")
root.geometry("300x250")
 
label1 = Label(text="Hello Python", fg="#eee", bg="#333")
label1.pack()
 
poetry = "Вот мысль, которой весь я предан,\nИтог всего, что ум скопил.\nЛишь тот, кем бой за жизнь изведан,\nЖизнь и свободу заслужил."
label2 = Label(text=poetry, justify=LEFT)
label2.place(relx=.1, rely=.3)
 
root.mainloop()
