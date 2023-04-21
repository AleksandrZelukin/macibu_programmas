from tkinter import *
logs = Tk()
logs.geometry("700x300+600+150")
logs.title('Mana pirma programma') 

def get_text():
    label2['text'] = text.get()

def get_text2():
    label2['text'] = text2.get(1.0, END)

def remove_text():
    label2.config(text="")
    
def iziet():
    logs.destroy()

def insert_text2():
    s = text.get()
    text2.insert(1.0, s)

frame1 = Frame(logs, highlightbackground="blue", highlightthickness=4)
frame1.grid(row=0,column=0)

frame2 = Frame(logs, highlightbackground="red", highlightthickness=4)
frame2.grid(row=2,column=0)

label1=Label(frame1,text='uzraksti savu vārdu')
label1.grid(row=0,column=0)

text = Entry(frame1)
text.grid(row=0,column=1)

text2 = Text(frame1,width=25, height=4)
text2.grid(row=0,column=3)

btn1=Button(frame1,text="Paņemt",command=get_text)
btn1.grid(row=0,column=2)

btn4=Button(frame1,text='Iekļaut',command=insert_text2)
btn4.grid(row=0,column=4)

btn2=Button(text="Beigt",command=iziet)
btn2.grid(row=2,column=0)

btn3=Button(frame1,text="Dzest",command=remove_text)
btn3.grid(row=1,column=1)

label2= Label(frame1)
label2.grid(row=1,column=0)


 
logs.mainloop()
