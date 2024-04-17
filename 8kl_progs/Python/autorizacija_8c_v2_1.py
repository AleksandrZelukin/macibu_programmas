import tkinter as tk
win = tk.Tk()
win.title("Ieeja sistēma")
win.geometry("300x400")
a = {"Ivars":"123","Olga":"123","Igors":"789"}
res = tk.Label(win, text = " ")
res.place(relx=.2, rely=.4)
nos = tk.Label(win, text = "Ievadiet Vārds u parole")
nos.place(relx=.2, rely=.0)

vards = tk.Entry()
vards.place(relx=.2, rely=.1)
parole = tk.Entry(win, show = '*')
parole.place(relx=.2, rely=.2)

def parbaude():
    vrd = vards.get()
    prl = parole.get()
    if a.get(vrd) != prl:
        res.configure(text="Lietotājvārds vai parole nesakrīt!")
    else:
        res.configure(text="OK!")

        
def exit():
    win.quit()
def smile():
    import smile
        
btn1 = tk.Button(text="Pārbaudit",command=parbaude)
btn1.place(relx=.2, rely=.3)
btn2 = tk.Button(text="Beigt",command=exit)
btn2.place(relx=.5, rely=.3)
btn3 = tk.Button(text="Atvērt programmu",command=smile)

btn3.place(relx=.4, rely=.4)

win.mainloop()