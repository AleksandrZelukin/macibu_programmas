from tkinter import *
root=Tk()
canvas= Canvas(root, width=400, height=250, bg="green")
canvas.create_rectangle(230, 10, 320, 80, outline="black", fill="yellow")
points = [100, 100, 100, 200, 200, 200]
canvas.create_polygon(points, outline="black", fill="red", width=2)
canvas.create_oval(10, 10, 80, 80, outline="gray", fill="gray", width=4)


canvas.pack()


root.mainloop()
