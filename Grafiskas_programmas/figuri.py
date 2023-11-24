import turtle as a

col = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

def fig1(x,y,size,z1,z2):
    a.pu()
    a.goto(x,y)
    a.pd()
    a.pensize(4)
    a.begin_fill()
    a.shape("turtle")
    for i in range (4):
        a.color(col[z1])
        a.fillcolor(col[z2])
        a.fd(size)
        a.lt(90)
    a.end_fill()

def fig2(x,y,size,z1,z2):
    a.pu()
    a.goto(x,y)
    a.pd()
    a.pensize(4)
    a.begin_fill()
    a.shape("turtle")
    for i in range (8):
        a.color(col[z1])
        a.fillcolor(col[z2])
        a.fd(size)
        a.lt(45)
    a.end_fill()

def fig3(x,y,size,z1,z2):
    a.pu()
    a.goto(x,y)
    a.pd()
    a.pensize(4)
    a.begin_fill()
    a.shape("turtle")
    for i in range (6):
        a.color(col[z1])
        a.fillcolor(col[z2])
        a.fd(size)
        a.lt(60)
    a.end_fill()
    
def star(x,y,size,z2):
    a.pu()
    a.goto(x,y)
    a.pd()
    a.pensize(4)
    a.begin_fill()
    for i in range (5):
        a.color(col[z2])
        a.fillcolor(col[z2])
        a.forward(size)
        a.right(144)
    a.end_fill()
    

fig1(-100,-200,150,0,4)
fig2(100,200,50,1,2)
fig3(-150,200,50,5,3)
star(-50,50,100,0)

a.mainloop()

