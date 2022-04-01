import tkinter as tk

# --- functions ---

def f(s):
    global w # inform function to use external variable when you will use `=`

    if s == "label":
        if w: # check if widget already exist
            w.destroy()

        w = tk.Label(root, text="Hello World!")
        w.grid(column=1, row=2)

    elif s == "button":
        if w: # check if widget already exist
            w.destroy()

        w = tk.Button(root, text="Click Me")
        w.grid(column=1, row=2)

    else:
        print('ERROR: unknow:', s)

# --- main ---

root = tk.Tk()
root.geometry("300x300+600+300")

v = tk.StringVar(value="f")

a = tk.OptionMenu(root, v, "label", "button", command=f)
a.grid(column=1, row=1)

w = None # create global variable without value
         # to use later with widget (and keep access to this widget)

root.mainloop()