from tkinter import *
import tkinter

logs=tkinter.Tk()
logs.title("Mana programma Tkinter ar pogu")
logs.geometry("400x800")
label1=Label(logs, text = 'Šeit ir jūsu teskst 1',
             font='14',
             background="#FF00AA",
            foreground="#00AAAA" )
label1.place(relx=0.5, rely=.5)

label2=Label(logs, text = 'Šeit ir jūsu teskst 2', font='12' )
label2.pack()

entry=Entry(logs,)
entry.place(relx=0.5, rely=.6)
btn1=tkinter.Button(text="Pirma poga",
            font="14",
            background="#FF0000",
            foreground="#0000AA",
            activebackground="#00FF00",
            padx="50",
            pady="20")

btn1.pack()

btn2=tkinter.Button(text="Otra poga",
            font="14",
            background="#FF0000",
            foreground="#0000AA",
            activebackground="#00FF00",)
btn2.place(relx=0.2, rely=.5)

btn3 = tkinter.Button(text="Treša poga", background="#555", foreground="#ccc",
              padx="15", pady="6", font="15")
btn3.pack(side = BOTTOM)

btn4 = tkinter.Button(text="Ceturta poga", background="#555", foreground="#ccc",
              padx="15", pady="6", font="15")
btn4.place(x=100, y=200)
'''
btn5 = tkinter.Button(text="Piekta poga", background="#555", foreground="#ccc",
              padx="15", pady="6", font="15")
btn5.grid(row = 5, column = 1)
btn6 = tkinter.Button(text="Sesta poga", background="#555", foreground="#ccc",
              padx="15", pady="6", font="15")
btn6.grid(row = 6, column = 2)
'''
logs.mainloop()

