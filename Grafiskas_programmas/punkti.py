import turtle as t
t.pu()
t.ht()
t.setpos(-500,500)

for n in range(10):
    for i in range(10):   
        t.fd (100)
        t.dot()
        t.write(t.pos())
        i+=1
