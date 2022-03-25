import tkinter as tk
win = tk.Tk()
win.title("Kalkulators")
win.geometry("400x400")
num1 = tk.Entry(win)
num1.grid(row = 0, column = 0)
num2 = tk.Entry(win)
num2.grid(row = 0, column = 1)
res = tk.Label(win, text = "-")
res.grid(row = 0, column = 3)


def summation():
    one = float(num1.get())
    two = float(num2.get())
    result = one + two
    #res.configure(text = "= %s" % result)
def reizinajums():
    one = float(num1.get())
    two = float(num2.get())
    result = one * two
    #res.configure(text = "= %s" % result)
def dalisana():
    one = float(num1.get())
    two = float(num2.get())
    result = one/two
    #res.configure(text = "= %s" % result)

def rezultats():
    res.configure(text = "= %s" % result)
    
button1 = tk.Button(win, text = "+", command = summation)
button1.grid(row = 0, column = 2)
button2 = tk.Button(win, text = "X", command = reizinajums)
button2.grid(row = 1, column = 2)
button3 = tk.Button(win, text = "/", command = dalisana)
button3.grid(row = 2, column = 2)
button4 = tk.Button(win, text = "=", command = rezultats)
button4.grid(row = 3, column = 2)
win.mainloop()
