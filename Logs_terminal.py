from tkinter import *
logs = Tk()
logs.geometry("400x400+300+300")





def Adarbība ():
    print("Paldies!")
def Bdarbība():
    print("Au! Man sāp!")

pogaA = Button(text='ķļikšņi te!', command=Adarbība)
pogaB = Button(text='Neķļikšņi te!', command=Bdarbība)

pogaB.pack(side=TOP)
pogaA.pack(side=BOTTOM)


logs.mainloop()
