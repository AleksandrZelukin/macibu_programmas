import tkinter as tk
win = tk.Tk()
win.title("Ieeja sistēma")
win.geometry("300x400")
a = {"Ivars":"123","Olga":"123","Igors":"789"}

res = tk.Label(win, text = " ")
res.place(relx=.2, rely=.4)
nos = tk.Label(win, text = "Ievadiet Vārds u parole")
nos.place(relx=.2, rely=.0)


def reizinajums():
    v = vards.get()
    p = parole.get()
    if a.get(v) != p:
        res.configure(text="Lietotājvārds vai parole nesakrīt!")
    else:
        res.configure("OK!")
        
vards = tk.Entry(win)
vards.place(relx=.2, rely=.1)
parole = tk.Entry(win)
parole.place(relx=.2, rely=.2)
   
button1 = tk.Button(win, text = "Ieeja",
                    background="#FF00AA",
                    foreground="#0000AA",
                    activebackground="#00FF00",
                    command=reizinajums)
button1.place (relx=.2, rely=.3)


win.mainloop()
