from random import *
from tkinter import *
izmērs = 400
logs = Tk()
audekls = Canvas(logs, width=izmērs*3, height=izmērs)
audekls.pack()
while True:
#    krāsa = choice(['pink', 'orange', 'purple', 'yellow'])
    krāsa = choice(['green', 'red', 'blue', 'yellow', 'pink', 'orange', 'purple'])
    x0 = randint(0, izmērs*3)
    y0 = randint(0, izmērs)
    d = randint(0, izmērs/2)
    audekls.create_oval(x0, y0, x0 + d, y0 +d, fill=krāsa)
    
    
    logs.update()
    
