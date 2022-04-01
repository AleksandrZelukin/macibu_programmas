import tkinter as tk

root = tk.Tk()
root.geometry("+600+300")

w = tk.Label(root, text="Pirmaias bloks Red Sun", bg="red", fg="white")
w.pack()
w = tk.Label(root, text="Green Grass", bg="green", fg="black")
w.pack()
w = tk.Label(root, text="Blue Sky", bg="blue", fg="white")
w.pack()


w = tk.Label(root, text="Otrais bloks Red Sun", bg="red", fg="white")
w.pack(fill=tk.X)
w = tk.Label(root, text="Green Grass", bg="green", fg="black")
w.pack(fill=tk.X)
w = tk.Label(root, text="Blue Sky", bg="blue", fg="white")
w.pack(fill=tk.X)


w = tk.Label(root, text="Tresais bloks Red Sun", bg="red", fg="white")
w.pack(fill=tk.X, padx=10)
w = tk.Label(root, text="Green Grass", bg="green", fg="black")
w.pack(fill=tk.X, padx=10)
w = tk.Label(root, text="Blue Sky", bg="blue", fg="white")
w.pack(fill=tk.X, padx=10)


w = tk.Label(root, text="Ceturtais bloks Red Sun", bg="red", fg="white")
w.pack(fill=tk.X, pady=10)
w = tk.Label(root, text="Green Grass", bg="green", fg="black")
w.pack(fill= tk.X, pady=10)
w = tk.Label(root, text="Blue Sky", bg="blue", fg="white")
w.pack(fill=tk.X, pady=10)

w = tk.Label(root, text="Piektais bloks Red Sun", bg="red", fg="white")
w.pack()
w = tk.Label(root, text="Green Grass", bg="green", fg="black")
w.pack(ipadx=10)
w = tk.Label(root, text="Blue Sky", bg="blue", fg="white")
w.pack()


w = tk.Label(root, text="Sestais bloks Red Sun", bg="red", fg="white")
w.pack()
w = tk.Label(root, text="Green Grass", bg="green", fg="black")
w.pack(ipadx=10)
w = tk.Label(root, text="Blue Sky", bg="blue", fg="white")
w.pack(ipady=10)


w = tk.Label(root, text="red", bg="red", fg="white")
w.pack(padx=5, pady=10, side=tk.LEFT)
w = tk.Label(root, text="green", bg="green", fg="black")
w.pack(padx=5, pady=20, side=tk.LEFT)
w = tk.Label(root, text="blue", bg="blue", fg="white")
w.pack(padx=5, pady=20, side=tk.LEFT)
'''
import random
languages = ['Python','Perl','C++','Java','Tcl/Tk']
labels = range(5)
for i in range(5):
   ct = [random.randrange(256) for x in range(3)]
   brightness = int(round(0.299*ct[0] + 0.587*ct[1] + 0.114*ct[2]))
   ct_hex = "%02x%02x%02x" % tuple(ct)
   bg_colour = '#' + "".join(ct_hex)
   l = tk.Label(root, 
                text=languages[i], 
                fg='White' if brightness < 120 else 'Black', 
                bg=bg_colour)
   l.place(x = 20, y = 30 + i*30, width=120, height=25)
   
'''
tk.mainloop()