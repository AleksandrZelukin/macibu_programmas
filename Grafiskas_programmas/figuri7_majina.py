from tkinter import *
root=Tk()
canvas=Canvas(root,width=600, height=400, bg="lightblue")

eka=(200,300,400,400) 
canvas.create_rectangle(eka, outline="black", fill="yellow")


logs=(250,320,350,390)
canvas.create_rectangle(logs,outline="black",fill="lightblue")

jumta = [200,300,300,200,400,300] 
canvas.create_polygon(jumta, outline="black", fill="red", width=2)

saule=(10,10,80,80)
canvas.create_oval(saule, outline="yellow", fill="yellow", width=4)

canvas.create_polygon(334, 228, 334,190, 350, 190, 350, 246, outline="black", fill="black")

canvas.create_text(300, 350, text="Sveiki,\n92.\nvidusskola",justify=CENTER, font="Arial 14")

canvas.pack()
poga=Button(text="Mana skola")
poga.pack()
root.mainloop()
