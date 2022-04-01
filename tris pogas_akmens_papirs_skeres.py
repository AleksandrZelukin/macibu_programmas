from tkinter import *
 
root = Tk()
root.title("tris pogas")
root.geometry("400x250+600+300")


label=Label(text="", font="Arial 24")
label.place(x=120, y=100)   


def label1 ():
    label.config(text="Jūs izvēlējat Akmenis", fg = "yellow", bg = "blue")
    


def label2 ():
    label.config(text="Jūs izvēlējat Šķeres.", fg = "yellow", bg = "red")
   
    

def label3 ():
    label.config(text="Jūs izvēlējat Papirs.", fg = "yellow", bg = "green")
    


    
    
btn1 = Button(text="Akmens", pady="7", font="13", command=label1)
btn1.place(x=10, y=20)
 
btn2 = Button(text="Škeres", pady="7", font="13",  command=label2)
btn2.place(x=10, y=80)
 
btn3 = Button(text="Papirs", pady="7", font="13", command=label3)
btn3.place(x=10, y=140)


btn5 = Button(text="Exit", command=root.destroy)
btn5.pack(side=BOTTOM)



root.mainloop()
