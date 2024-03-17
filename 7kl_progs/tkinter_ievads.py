from tkinter import *
logs = Tk()
logs.geometry('800x600+600+100')

def izeja():
    print('Programma beidza savu darbu')
    logs.destroy()

def vards():
    label3["text"] = entry.get()

label1=Label(logs,text="Sveiki!",fg='blue',font=('Arial',32))
# label1.place(relx=0.1,rely=0.1)
# label1.grid(row=0,column=0)
label1.pack( padx=25, pady=25)
label1.place(x=100,y=20)

label2=Label(logs,text="Kur tu dzivo?",fg='red',font=('Arial',32))
# label2.place(relx=0.4,rely=0.1)
# label2.grid(row=0,column=1)
label2.pack(padx=15, pady=20)


entry=Entry(font=('Arial',32))
# entry.place(relx=0.6,rely=0.1)
# entry.grid(row=1,column=1)
entry.pack(padx=15, pady=20)

label3=Label( font=('Arial',32))
label3.pack(padx=15, pady=20)

btn1=Button(logs,text='Saglābat', fg='yellow',bg='blue',font=('Arial',32),command=vards)
# btn1.place(relx=0.1,rely=0.3)
# btn1.grid(row=2,column=0)
btn1.pack(padx=15, pady=20)

btn2=Button(logs,text='Beigt', fg='yellow',bg='red',font=('Arial',32),command=izeja)
# btn2.place(relx=0.4,rely=0.3)
# btn2.grid(row=2,column=1)
btn2.pack(side=BOTTOM, padx=15, pady=20)

logs.mainloop()


