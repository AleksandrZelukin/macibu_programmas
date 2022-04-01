from tkinter import*

a=Tk()
a.title("Mana poga")

a.geometry("600x600")
b=Button(text="Press me", background="red",foreground="blue", padx="15", pady="6",font="45")
b.pack(expand=True, fill=BOTH)

a.mainloop()
