from random import *
from tkinter import *
izmērs = 1000
logs = Tk()
audekls = Canvas(logs, width=izmērs, height=izmērs)
audekls.pack()
while True:
#    krāsa = choice(['pink', 'orange', 'purple', 'yellow'])
    krāsa = choice(['green', 'red', 'blue', 'yellow'])
    x0 = randint(0, izmērs)
    y0 = randint(0, izmērs)
    d = randint(0, izmērs/5)
    audekls.create_oval(x0, y0, x0 + d, y0 +d, fill=krāsa)
    logs.update()
