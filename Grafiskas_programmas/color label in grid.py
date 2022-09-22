import tkinter as tk


colours = ['red','green','orange','white','yellow','blue']

r = 0
for c in colours:
    tk.Label(text=c, relief=tk.RIDGE, width=15, bg=c).grid(row=r,column=0)
    tk.Entry(bg=c, relief=tk.SUNKEN, width=10).grid(row=r,column=1)
    tk.Button(text=c, fg=c).grid(row=r,column=2)
    r = r + 1

tk.mainloop()
#https://www.python-course.eu/tkinter_layout_management.php