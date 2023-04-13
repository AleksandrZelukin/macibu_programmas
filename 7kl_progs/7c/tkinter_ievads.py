from tkinter import *
logs = Tk()
logs.geometry('800x600+600+100')
label1=Label(logs,text="Sveiki!",fg='blue',font=('Arial',32))
label2=Label(logs,text="Latvija!",fg='red',font=('Arial',32))
entry=Entry(font=('Arial',32))
btn1=Button(logs,text='Sākums', fg='yellow',bg='blue',font=('Arial',32))

label1.pack()
label2.pack()
entry.pack()
btn1.pack()


mainloop()