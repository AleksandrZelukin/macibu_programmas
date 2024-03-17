from tkinter import *

root = Tk()

root.geometry('800x600')

btn1=Button(text='POGA DAŽADU KRĀSA',font=24,background='#ff0000',foreground='#00ff00',width=20)
btn1.grid(row=0,column=0)

btn2=Button(text='POGA DAŽADU KRĀSA',font=24,background='#0000ff',foreground='#00ffff',width=20)
btn2.grid(row=1,column=1)

btn3=Button(text='POGA DAŽADU KRĀSA',font=24,background='#ff00ff',foreground='#ffff00',width=20)
btn3.grid(row=2,column=2)

btn4=Button(text='',font=24,background='#ff0000',foreground='#00ff00',width=20)
btn4.grid(row=3,column=3)

btn5=Button(text='',font=24,background='#0000ff',foreground='#00ffff',width=20)
btn5.grid(row=4,column=1)

btn6=Button(text='',font=24,background='#ff00ff',foreground='#ffff00',width=20)
btn6.grid(row=5,column=0)


mainloop()