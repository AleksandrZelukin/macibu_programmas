from tkinter import *
logs = Tk()
logs.geometry('800x800+600+150')


label1 = Label(text='Hello world!',font=('Alrial','24','bold'),bg='blue',fg='yellow')
entry1 = Entry(font=('Alrial','24','bold'),fg='yellow')
btn1 = Button(text='Press Me!',font=('Alrial','24','bold'),bg='red',fg='blue')


label1.pack()
entry1.pack()
btn1.pack()

logs.mainloop()