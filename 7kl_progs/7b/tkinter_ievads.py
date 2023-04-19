from tkinter import *
logs = Tk()
logs.geometry("800x800+600+100")

def pilseta():
    label3['text']=entry1.get()

def izeja():
    print('Programma beidz darbu!')
    logs.destroy()
    
label1=Label(text="Sveiki draugs!",font=('Arial','24'))
label1.place(x=0,y=20)

label2=Label(text="Kur tu dzivo?",font=('Arial','24'))
label2.place(x=0,y=100)

label3=Label(font=('Arial','24'))
label3.place(x=300,y=200)

entry1=Entry(font=('Arial','24'))
entry1.place(x=300,y=100)

btn1=Button(text="Ievads",font=('Arial','24'),bg='green',fg="blue",command=pilseta)
btn1.place(x=360,y=260)

btn2=Button(text="Izeja",font=('Arial','24'),bg='red',fg='blue',command=izeja)
btn2.place(x=360,y=400)

mainloop()