from tkinter import *
win = Tk()
win.geometry('800x800+700+150')

label1 = Label(text='Hello World!',font=('Arial','24'),bg='green',fg='blue')
btn1 = Button(text='Press me!',font=('Arial','24'),bg='red',fg='yellow')
entry1 = Entry(font=('Arial','24'),fg='blue')

label1.pack()
entry1.pack()
btn1.pack()

win.mainloop()