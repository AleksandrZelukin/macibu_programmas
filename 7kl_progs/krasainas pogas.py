from tkinter import *
logs = Tk()
logs.geometry('700x800+600+100')
logs.title('Visas krāsas varaviksnē')
def fons1 ():
    logs.configure(bg='blue')
    
def fons2 ():
    logs.configure(bg='red')

def fons3 ():
    logs.configure(bg='yellow')
def izeja():
    print('Programma beidza savu darbu')
    logs.destroy()
 
label1=Label(logs,text="Visas krāsas varaviksnē",fg='blue',font=('Arial',16))
label1.grid(row=0,column=1,padx=10,pady=10)

label2=Label(font=('Arial',16))
label2.grid(row=1,column=1,pady=10)
btn1=Button(logs,text='Red', fg='#000000',bg='#ff0000',font=('Arial',16),width=14,command=fons1)
btn1.grid(row=2,column=0,padx=20, pady=10)
btn2=Button(logs,text='Orange', fg='#000000',bg='#00a500',font=('Arial',16),width=14,command=fons2)
btn2.grid(row=2,column=1,pady=10)
btn3=Button(logs,text='Yellow', fg='#000000',bg='#ffff00',font=('Arial',16),width=14,command=fons3)
btn3.grid(row=2,column=2,pady=10)
btn4=Button(logs,text='Green', fg='#000000',bg='#008000',font=('Arial',16),width=14,command=fons1)
btn4.grid(row=3,column=0,pady=10)
btn5=Button(logs,text='Blue', fg='#000000',bg='#0000ff',font=('Arial',16),width=14,command=fons2)
btn5.grid(row=3,column=1,pady=10)
btn6=Button(logs,text='Indigo', fg='#ffaa00',bg='#4b0082',font=('Arial',16),width=14,command=fons3)
btn6.grid(row=3,column=2,pady=10)
btn7=Button(logs,text='Violet', fg='#000000',bg='#ee82ee',font=('Arial',16),width=14,command=fons1)
btn7.grid(row=4,column=1,pady=10)
btn8=Button(text='Izeja',height=1,font=('Arial',32,'bold'),width=4, fg='#aaaa00',bg='#ff0000',command=izeja)
btn8.grid(row=5,column=1)
mainloop()