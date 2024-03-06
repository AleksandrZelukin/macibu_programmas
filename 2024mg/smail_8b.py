import tkinter as tk
import turtle as tu
logs = tk.Tk()
#window.title("8b pogas")
#window.geometry("600x600")
tu.home()


def button_click():
    logs.destroy()

button = tk.Button(text="Close window", command=button_click)
button.pack()


logs.mainloop()