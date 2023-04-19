from tkinter import *
logs = Tk()
logs.geometry('800x800+600+150')

def izeja():
    print('Programma beidz savu darbu')
    logs.destroy()
def teksts():
    print('Sveiki, draugs!')
    label2["text"] = entry1.get()
    
    
label1 = Label(text='Hello world!',font=('Alrial','24','bold'),bg='blue',fg='yellow')
entry1 = Entry(font=('Alrial','24','bold'),fg='darkblue')
btn1 = Button(text='Press Me!',font=('Alrial','24','bold'),bg='green',fg='blue',command=teksts)
btn2 = Button(text='IZEJA!',font=('Alrial','24','bold'),bg='red',fg='blue',command=izeja)
label2 = Label(font=('Alrial','24','bold'),fg='blue')
label1.grid(row=0,column=0)
entry1.grid(row=0,column=1)
btn1.grid(row=0,column=2)
btn2.grid(row=1,column=1)
label2.grid(row=2,column=1)
logs.mainloop()