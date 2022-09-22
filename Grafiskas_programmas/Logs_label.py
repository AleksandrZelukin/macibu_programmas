from tkinter import *
logs = Tk()
logs.geometry("400x400+300+300")
logs.title("ķļikšņi man")


label=Label(text="", font="Arial 24")
label.pack(padx=20, pady=100)   

def Adarbiba ():
    label.config(text="Paldies!")
def Bdarbiba ():
    label.config(text="Au! Man sāp!")
   
pogaA = Button(logs, text='ķļikšņi te!', command=Adarbiba)
pogaB = Button(logs, text='Neķļikšņi te!', command=Bdarbiba)


pogaA.pack(padx=20, pady=30)
pogaB.pack(padx=1, pady=1)


logs.mainloop()
