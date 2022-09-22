from tkinter import *
root=Tk()
canvas= Canvas(root, width=400, height=250, bg="green")
canvas.create_rectangle(230, 10, 320, 80, outline="black", fill="yellow")
points = [100, 100, 100, 200, 200, 200]
canvas.create_polygon(points, outline="black", fill="red", width=2)
canvas.create_oval(10, 10, 80, 80, outline="gray", fill="gray", width=4)


canvas.create_text(200, 100, text="Sveiki,\n92.\nvidusskola",justify=CENTER, font="Arial 14")


canvas.pack()

poga=Button(text="Canvas")
poga.pack()

root.mainloop()
