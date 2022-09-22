import turtle

sc = turtle.Screen()
bo = turtle.Turtle()

#screen

sc.bgcolor("black")
sc.title("tic tac toe")

#board

bo.color("white")
bo.penup()
bo.speed(0)
bo.setposition(-100, -300)
bo.pendown()
bo.setposition(-100, 300)
bo.penup()
bo.setposition(100, 300)
bo.pendown()
bo.setposition(100, -300)
bo.penup()
bo.setposition(-300, 100)
bo.pendown()
bo.setposition(300, 100)
bo.penup()
bo.setposition(300, -100)
bo.pendown()
bo.setposition(-300,-100)
bo.penup()
bo.setposition(0,0)

#naught and cross function

def c()  :
    bo.pendown()
    x = bo.xcor()-80
    y = bo.ycor()+80
    bo.penup()
    bo.setposition(x,y)
    bo.pendown()
    x = bo.xcor()+160
    y = bo.ycor()-160
    bo.setposition(x,y)
    bo.penup()
    x = bo.xcor()-160
    bo.setposition(x,y)
    bo.pendown()
    x = bo.xcor()+160
    y = bo.ycor()+160
    bo.setposition(x,y)
    bo.penup()
    bo.setposition(0,0)

def n() :
    y = bo.ycor()-80
    x = bo.xcor()
    bo.setposition(x, y)
    bo.pendown()
    bo.circle(80)
    bo.penup()
    bo.setposition(0,0)

#movment
def move_left(event):
    x = bo.xcor()
    x -= 200
    if x < -300:
        x = -200
    bo.setx(x)

def move_right(event):
    x = bo.xcor()
    x += 200
    if x > 300:
        x = 200
    bo.setx(x)

def move_down(event):
    y = bo.ycor()
    y -= 200
    if y < -300:
        y = -200
    bo.sety(y)

def move_up(event):
    y = bo.ycor()
    y += 200
    if y > 300:
        y = 200
    bo.sety(y)

#Keybinding

turtle.listen()

turtle.getcanvas().bind("<Left>", move_left)
turtle.getcanvas().bind("<Right>", move_right)
turtle.getcanvas().bind("<Up>", move_up)
turtle.getcanvas().bind("<Down>", move_down)
