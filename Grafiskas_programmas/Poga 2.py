from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("Mana poga")
root.geometry("600x400")
# root.color("red")


click = 0

def click_button ():
    global click
    click += 1
    root.title("Click {}".format(click))



def show_message():
    messagebox.showinfo("GUI Python", message.get())

message = StringVar()
 
message_entry = Entry(textvariable=message)
message_entry.place(relx=.5, rely=.1, anchor="c")
    
btn2 = Button(text="Click me",
             padx="40",
             pady="20",
             font="18",
             command=show_message)
btn2.pack(padx="20",
         pady="60")


btn1 = Button(text="start!",
             fg="#222",
             bg="#eee",
             padx="40",
             pady="20",
             font="18",
              command=click_button)
btn1.pack(padx="20",
         pady="10")



label1 = Label(text="Hello Python", fg="#eee", bg="#333")
label1.pack()



root.mainloop()
