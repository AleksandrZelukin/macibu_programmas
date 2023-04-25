from tkinter import *
logs = Tk()
logs.geometry('800x600+600+100')

def izeja():
    print('Programma beidza savu darbu')
    logs.destroy()


   
label1=Label(logs,text="Sveiki!",fg='blue',font=('Arial',32))
label1.pack()


label2=Label(font=('Arial',32))
btn1=Button(logs,text='Dažadu krāses poga', fg='yellow',bg='blue',font=('Arial',32),command=izeja)
btn1.pack()
mainloop()