import tkinter as tk

# --- functions ---

def generate():
    try:
        result = float(num1.get()) + float(num2.get())
    except Exception as ex:
        print(ex)
        result = 'error'

    num3.set(result)

# --- main ---

root = tk.Tk()

num1 = tk.StringVar()
num2 = tk.StringVar()
num3 = tk.StringVar()

tk.Label(root, text="Number 1:").grid(row=0, column=0)
tk.Label(root, text="Number 2:").grid(row=1, column=0)
tk.Label(root, text="Result:").grid(row=2, column=0)

tk.Entry(root, textvariable=num1).grid(row=0, column=1)
tk.Entry(root, textvariable=num2).grid(row=1, column=1)
tk.Entry(root, textvariable=num3).grid(row=2, column=1)

button = tk.Button(root, text="Calculate", command=generate)
button.grid(row=3, column=1)

root.mainloop()
