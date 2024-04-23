from tkinter import *
logs = Tk()
logs.title("Skolotājs")
logs.geometry("300x600")
a = {"Ivars":"123","Aija":"345"}
nos = Label(text="Ivadiet Lietotājvārds un Parole")
nos.pack()
vards = Entry()
vards.pack()
parole = Entry(show="*")
parole.pack()
rez = Label(text="").pack()
def parbaude():
    v = str(vards.get())
    p = str(parole.get())
    if a.get(v) != p:
        rez.configure(text="Lietotājvārds vai parole nesakrīt!")
    else:
        rez.configure(text="OK!")
def iziet():
    logs.destroy()        
btn1 = Button(text="Pārbaudit!",command=parbaude).pack()

btn2 = Button(text="Beigt",command=iziet).pack()


logs.mainloop()