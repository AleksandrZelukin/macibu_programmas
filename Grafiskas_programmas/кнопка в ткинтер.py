from tkinter import * 

root = Tk()
root.geometry("300x200")

def func(event):
    print("You hit return.")

def onclick(event):
    print("You clicked the button")

root.bind('<Return>', onclick)

button = Button(root, text="click me", command=onclick)
button.bind('<Button-1>', onclick)
button.pack()

root.mainloop()

