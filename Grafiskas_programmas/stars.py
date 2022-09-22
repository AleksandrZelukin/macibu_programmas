from tkinter import *
from random import randrange as rnd, choice 
import math, time

colors = ['red','orange','yellow','green','cyan','blue','magenta','black','gray','lightgreen']

root = Tk()
root.geometry('400x400')

canv = Canvas(root, bg = 'white')
canv.pack(fill = BOTH, expand = 1)
def star(x0=400,y0=300,r1=100,r2=30,col1='lightgreen',col2='green',da=12):
    a1 = 0
    a2 = 0
    a = []
    da = 360//da
    for a1 in range(da//2,360+da,da):
        y1 = x0 + r1*math.sin(a1*math.pi/180)
        x1 = y0 + r1*math.cos(a1*math.pi/180)
        a += [(x1,y1)]
        y2 = x0 + r2*math.sin((a1+da//2)*math.pi/180)
        x2 = y0 + r2*math.cos((a1+da//2)*math.pi/180)
        a += [(x2,y2)]
    canv.create_polygon(a, fill = col1, outline = col2, width = 2)

for zz in range(3,22):	
    for z in range(30):
        r1 = rnd(20,100)
        r2 = rnd(20,50)
        x = 200
        y = 200
        star(x,y,r1,r2,choice(colors),choice(colors),zz)
        time.sleep(0.1)
        canv.update()
    time.sleep(0.8)
    canv.delete(ALL)

mainloop()