from tkinter import *

root = Tk()

root.geometry('600x600')

btn1=Button(text='POGA DAŽADU KRĀSA',font=24,background='#ff0000',foreground='#00ff00')
btn1.pack(side=BOTTOM, pady=10)

btn2=Button(text='POGA DAŽADU KRĀSA',font=24,background='#0000ff',foreground='#00ffff')
btn2.pack(side=BOTTOM, pady=0)

btn3=Button(text='POGA DAŽADU KRĀSA',font=24,background='#ff00ff',foreground='#ffff00')
btn3.pack(side=BOTTOM, pady=10)
mainloop()