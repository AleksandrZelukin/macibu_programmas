from tkinter import *
 
logs = Tk()
logs.title("Mana programma Tkinter")
logs.geometry("600x600")


label1 = Label(text="")
#label1.pack()
label1.place(relx=.5, rely=.10)


label2=Label(text="")
#label2.pack()
label2.place(relx=.5, rely=.20)

def A ():
    print("Paldies")

def B ():
    print("mani sauc Andris")

def write_text1():
    label1.config(text="Paldies")

def write_text2():
    label2.config(text="mani sauc Andris")
    
btn = Button(text="Press Me!",background="red",foreground="blue",padx="20",pady="8",font="16", command=write_text1)
btn.place(relx=.1, rely=.10)

btn2 = Button(text="Ka tev sauc?",background="blue",foreground="blue",padx="20",pady="8",font="16", command=write_text2)
btn2.place(relx=.1, rely=.20)
#btn2.place(x="10", y="160")


def quit1():
     logs.destroy()

btn3 = Button(text="Close",background="blue",foreground="red",padx="20",pady="8",font="16", command=quit1)
#btn3.pack()

btn3.place(relx=.1, rely=.40)

logs.mainloop()
