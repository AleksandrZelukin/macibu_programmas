# Import Module
from tkinter import *

# Create Object
root = Tk()

# specify size of window.
root.geometry("400x400")

# Remove text from label
def write_text1():
    label.config(text="Sveiki  1")

def write_text2():
    label.config(text="Sveiki    2")
    
def write_text3():
    label.config(text="Sveiki      3")

def remove_text():
    label.config(text="")
    

# Create Label
#label = Label(root, text="Hello World!", font="BOLD")
label = Label(text="")
label.pack()
label.place(x=120, y=100)
# Create Delete Button
Button(root, text="Delete", command=remove_text).pack()

Button(root, text="Write1", command=write_text1).pack()

Button(root, text="Write2", command=write_text2).pack()

Button(root, text="Write3", command=write_text3).pack()

# Excute Tkinter
root.mainloop()

