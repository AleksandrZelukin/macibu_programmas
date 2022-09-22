from tkinter import *

root=Tk()


click = 0

def click_button ():
    global click
    click += 1
    root.title("Click {}".format(click))



c= Canvas(root, width=600, height=400, bg="lightblue")

c.pack()

c.create_rectangle(100, 100, 300, 300, outline="#fb0", fill="#fb0")


points = [150, 100, 200, 120, 240, 180, 210, 200, 150, 150, 100, 200]


c.create_polygon(points, outline="red", fill="green", width=2)


c.create_oval(300, 200, 400, 300, outline="gray", fill="yellow", width=2)





btn1 = Button(text="start!",
             fg="#222",
             bg="#eee",
             padx="40",
             pady="20",
             font="18",
              command=click_button)
btn1.pack(padx="20",
         pady="10")

c.pack()
root.mainloop()
