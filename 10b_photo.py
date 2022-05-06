from tkinter import *

logs = Tk()
logs.title("Rīgas 92.vidusskolas emblēma")
logs.geometry("600x600")
textLabel = Label(logs, text="Rīgas 92.vidusskola",justify=CENTER,padx=10)
textLabel.pack(side=BOTTOM)

photo = PhotoImage(file="92 vsk logo.png")
imgLabel = Label(logs, image=photo)
imgLabel.pack()

mainloop()
