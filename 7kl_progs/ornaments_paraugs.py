import turtle
turtle.shape("circle")
turtle.shapesize(0.5)
for i in range(36):   
    turtle.fd(30)
    turtle.lt(10)
    turtle.stamp()
turtle.goto(0,60)   
for k in range(36):
    turtle.fd(20)
    turtle.lt(10)
    turtle.stamp()

while True:
    turtle.forward(200)
    turtle.left(170)
    if abs(turtle.pos()) < 1:
        break

turtle.mainloop()