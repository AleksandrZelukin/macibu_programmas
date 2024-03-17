from turtle import *
import tkinter as tk
t = Turtle()

krasa = ("red","yellow","blue","lightblue","black")
speed(1000)
def saule():
    pu()
    goto(-300,160)
    pd()
    fillcolor(krasa[1])
    pencolor(krasa[1])
    begin_fill()
    for i in range(36):
        fd(200)
        rt(180)
        rt(10)
    end_fill()
    pencolor(krasa[4])
    write("Tas ir SAULE!", align='left', font=('Arial', 18, 'bold'))

pencolor(krasa[0])
def figura(x,y,z,n,m):
    pu()
    goto(x,y)
    pd()
    fillcolor(krasa[m])
    begin_fill()
    for i in range(n):
        fd(z)
        lt(360/n)
    end_fill()
    
def truba(x,y,z,m):
    pu()
    goto(x,y)
    pd()
    fillcolor(krasa[m])
    begin_fill()
    fd(z-40)
    lt(90)
    fd(z)
    lt(90)
    fd(z-40)
    lt(90)
    fd(z)
    lt(90)
    end_fill()
          
def siena ():
    figura(-75,-380,150,4,0)
def durvis():
    truba(-60,-380,80,3)
def logs():
    figura(10,-300,40,4,3)
def caurule ():
    truba(20,-122,60,0)
def jumta():
    truba(20,-122,60,0)
    figura(-100,-230,200,3,1)
    

poga1 = tk.Button(text="SAULE",command=saule)
#poga1.place(x=260,y=140)
poga1.place(relx=.4,rely=.2)
poga2 = tk.Button(text="SIENA",command=siena)
#poga2.place(x=40,y=70)
poga2.place(relx=.5,rely=.2)
poga3 = tk.Button(text="DURVIS",command=durvis)
#poga3.place(x=40,y=100)
poga3.place(relx=.6,rely=.2)
poga4 = tk.Button(text="JUMTA",command=jumta)
#poga4.place(x=40,y=130)
poga4.place(relx=.7,rely=.2)
poga5 = tk.Button(text="LOGS", command=logs)
#poga5.place(x=40,y=160)
poga5.place(relx=.8,rely=.2)  


mainloop()


#pencolor(krasa[4])
#write("Tas ir DŪMENIS!", align='left', font=('Arial', 18, 'bold'))  