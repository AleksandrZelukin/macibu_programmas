from tkinter import *
root=Tk()
canvas= Canvas(root, width=400, height=250)
canvas.create_rectangle(230, 10, 320, 80, outline="black", fill="yellow")


canvas.create_oval(10, 10, 80, 80, outline="gray", fill="gray", width=4)




canvas.pack()



root.mainloop()
