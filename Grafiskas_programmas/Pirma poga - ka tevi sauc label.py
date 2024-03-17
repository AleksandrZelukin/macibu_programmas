from tkinter import *

a=Tk()

a.title("Skolotāja poga")
a.geometry("800x800")

text = Text(width=25, height=5, bg="lightblue")
text.pack(ipadx=100, ipady=5)

text = Entry(width=20, bg="lightblue")
text.pack(ipadx=100, ipady=5)

#frame = Frame()
#frame.pack()

label = Label()
label.place(relx=0.5, rely=0.1)

label1=Label(text="")
label1.place(relx=0.3, rely=0.1)

label2=Label(text="")
label2.place(relx=0.3, rely=0.2)

def A():
    #print("Ka tev sauc?")
    label1.config(text="Ka tev sauc?")

    
def B():
    #print ("Kur tu dzivo?")
    label2.config(text="Kur tu dzivo?")

def get_text():
    s = text.get(1.0, END)
    label['text'] = s
    
def quit():
     a.destroy()

    
    
#b=a.Entry(master)   

btn1 = Button(text="Poga 1",bg="red",fg="blue",padx="20",pady="1",font="16", command=A)


btn1.place(relx=0.1, rely=0.1)

btn2 = Button(text="Poga 2",background="lightgreen",foreground="blue",padx="20",pady="1",font="16", command=B)


btn2.place(relx=0.1, rely=0.2)

btn3 = Button(text="Poga 3",background="yellow",foreground="blue",padx="20",pady="1",font="16", command=get_text)


btn3.place(relx=0.1, rely=0.3)

btn4 = Button(text="Beigt",background="yellow",foreground="blue",padx="30",pady="1",font="16", command=quit)


btn4.place(relx=0.1, rely=0.4)


a.mainloop()
