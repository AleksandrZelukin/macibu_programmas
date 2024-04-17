from tkinter import Tk,Label,Entry,Button
logs = Tk()
logs.title("Ieeja sistēma")
logs.geometry("300x400")
a = {"Anna":"123","Ivars":"456","Anna":"792"}
nos = Label(text="Ievadi lietotājavards un parole")
nos.pack()
vards = Entry()
vards.pack()
parole = Entry(show="*")
parole.pack()


def parbaude():
    v = vards.get()
    p = parole.get()
    if a.get(v) != p:
        rezultats.configure(text="Lietotājvards vai parole nesakrīt!")
    else:
        rezultats.configure(text="OK!")

def close():
   logs.quit()        
    
btn = Button(text="Pārbaudit",command=parbaude)
btn.pack()
rezultats = Label(text="")
rezultats.pack()

btn1 = Button(text="Beigt",command=close)
btn1.pack()

logs.mainloop()