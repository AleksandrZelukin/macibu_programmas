import turtle

def moveUp():
    x, y = pen.position()
    pen.setposition(x, y + speed)

def moveDown():
    x, y = pen.position()
    pen.setposition(x, y - speed)

def moveRight():
    x, y = pen.position()
    pen.setposition(x + speed, y)

def moveLeft():
    x, y = pen.position()
    pen.setposition(x - speed, y)

def change():
    if pen.isvisible():
        pen.up()
        pen.hideturtle()
    else:
        pen.down()
        pen.showturtle()

def speedUP():
    global speed
    speed += 1

def speedDOWN():
    global speed
    speed = max(0, speed + 1)

window = turtle.Screen()
pen = turtle.Turtle()
speed = 5

window.onkey(moveUp, "Up")
window.onkey(moveDown, "Down")
window.onkey(moveRight, "Right")
window.onkey(moveLeft, "Left")
window.onkey(change, "space")
window.onkey(speedUP, "q")
window.onkey(speedDOWN, "w")
window.listen()
window.mainloop()
