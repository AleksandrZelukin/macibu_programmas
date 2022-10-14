from tkinter import *
import random

root = Tk()
root.title("tris pogas")
root.geometry("450x250+600+300")


label=Label(text="", font="Arial 24")
label.place(x=120, y=100)   
player = 0
comp = 0

def akmens ():
    label.config(text="Jūs izvēlējas Akmens", fg = "yellow", bg = "blue")
    print("Jūs izvēlējas Akmens")
    player == 1
    
    
def skeres ():
    label.config(text="Jūs izvēlējas Šķeres.", fg = "yellow", bg = "red")
    print("Jūs izvēlējas Šķeres")
    player == 2
    

def papirs ():
    label.config(text="Jūs izvēlējas Papirs.", fg = "yellow", bg = "green")
    print("Jūs izvēlējas Papirs")
    player == 3

def computer():
    return random.choice(1,2,3)


def resultat(player,comp):
    player
    comp
    





btn1 = Button(text="Akmens", pady="7", font="13", command=akmens)
btn1.place(x=10, y=20)
 
btn2 = Button(text="Škeres", pady="7", font="13",  command=skeres)
btn2.place(x=10, y=80)
 
btn3 = Button(text="Papirs", pady="7", font="13", command=papirs)
btn3.place(x=10, y=140)

btn4 = Button(text="Exit", command=root.destroy)
btn4.pack(side=BOTTOM)


root.mainloop()
