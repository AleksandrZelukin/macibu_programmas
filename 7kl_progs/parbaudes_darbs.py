from tkinter import *
logs = Tk()
logs.geometry('800x600+600+100')

def izeja():
    print('Programma beidza savu darbu')
    logs.destroy()

def reizinajums():
    one = float(entry1.get())
    two = float(entry2.get())
    result = str(one * two)
    print(result)
    label2.config(result)
   
label1=Label(logs,text="Sveiki!",fg='blue',font=('Arial',32))
label1.pack()

entry1 = Entry(font=('Arial',32))
entry1.pack()
entry2 = Entry(font=('Arial',32))
entry2.pack()
label2=Label(font=('Arial',32))
btn1=Button(logs,text='reizināšana', fg='yellow',bg='blue',font=('Arial',32),command=reizinajums)
btn1.pack()
mainloop()