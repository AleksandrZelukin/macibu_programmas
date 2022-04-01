import tkinter as tk

# --- functions ---

def f(s):
    if s == "btn":
        l['text'] = "one blah blah"
    elif s == "btn2":
        l['text'] = "two"
    else:
        print('ERROR: unknow:', s)

# --- main ---

root = tk.Tk()
root.geometry("200x200+600+300")

v = tk.StringVar(value="f")

a = tk.OptionMenu(root, v, "btn", "btn2", command=f)
a.grid(column=1, row=1)

l = tk.Label(root)
l.grid(column=1, row=2)

root.mainloop()