from tkinter import *
root=Tk()
canvas= Canvas(root, width=400, height=250, bg="green")
canvas.create_rectangle(230, 10, 320, 80, outline="black", fill="yellow")
points = [100, 100, 100, 200, 200, 200]
canvas.create_polygon(points, outline="black", fill="red", width=2)
canvas.create_oval(10, 10, 80, 80, outline="gray", fill="yellow", width=4)
canvas.create_oval(200,200,125,125, outline="gray", fill="yellow", width=4)


canvas.create_text(200, 100, text="Sveiki,\n92.\vidusskola",justify=CENTER, font="Arial 14")
canvas.create_text(250, 250, text="Autors 10.b skolnieks",anchor=SE, fill="lightgrey")

canvas.pack()

poga=Button(text="Canvas")
poga.pack()

root.mainloop()
