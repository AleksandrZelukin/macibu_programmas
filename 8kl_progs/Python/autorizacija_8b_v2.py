from tkinter import *
logs = Tk()
logs.title("Skolotājs")
logs.geometry("300x600")
nos = Label(text="Ivadiet Lietotājvārds un parole")
nos.pack()
vards = Entry()
vards.pack()
logs.mainloop()