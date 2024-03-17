from tkinter import *
 
root = Tk()

root.geometry("300x250")

 
btn1 = Button(text="BOTTOM", background="#555", foreground="#ccc",
              padx="15", pady="6", font="15")
btn1.pack(side=BOTTOM)
 
btn2 = Button(text="RIGHT", background="#555", foreground="#ccc",
             padx="15", pady="6", font="15")
btn2.pack(side=BOTTOM)
 
btn3 = Button(text="LEFT", background="#555", foreground="#ccc",
             padx="15", pady="6", font="15")
btn3.pack(side=BOTTOM)
 
btn4 = Button(text="TOP", background="#555", foreground="#ccc",
             padx="15", pady="6", font="15")
btn4.pack(side=BOTTOM)
 
root.mainloop()
