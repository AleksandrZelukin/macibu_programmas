from tkinter import *

logs=Tk()
logs.title("Mana programma Tkinter ar pogu")
logs.geometry("400x800")

btn1=Button(text="Pirma poga",
            font="14",
            background="#FF0000",
            foreground="#0000AA",
            activebackground="#00FF00",
            padx="150",
            pady="50")
#btn1.place(relx=.1, rely=.2)
btn1.pack()

btn2=Button(text="Otra poga",
            font="14",
            background="#00FF00",
            foreground="#0000AA",
            activebackground="#FFFF00",
            width="50",
            height="5")
#btn2.place(relx=.1, rely=.4)
btn2.pack()

btn3=Button(text="Treša poga",
            font="14",
            background="#0000DD",
            foreground="#00DDAA",
            activebackground="#00FFFF",
            width="50",
            height="5")
#btn3.place(relx=.1, rely=.4)
btn3.pack()

logs.mainloop()

