import turtle as t
t.shape("turtle")

t.up()
t.goto(-100,-150)
t.down()
t.fillcolor("lightblue")
t.begin_fill()
for i in range (4):
    t.fd(200)
    t.rt(90)

for i in range (3):
    t.fd(200)
    t.lt(120)
t.end_fill()

t.up()
t.goto(-200,150)
t.down()
t.color("yellow")
t.fillcolor("yellow")
t.begin_fill()
t.pensize(4)
for i in range (10):
    t.fd(200)
    t.bk(200)
    t.lt(36)
t.goto(-200,100)
t.circle(50)
t.end_fill()

t.mainloop()