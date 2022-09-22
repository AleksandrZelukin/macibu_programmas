import tkinter

logs=tkinter.Tk()
logs.title("Mana programma Tkinter ar pogu")
logs.geometry("400x800")

btn1=tkinter.Button(text="Pirma poga",
            font="14",
            background="#FF0000",
            foreground="#0000AA",
            activebackground="#00FF00",
            padx="150",
            pady="50")
#btn1.place(relx=.1, rely=.2)
btn1.pack()
