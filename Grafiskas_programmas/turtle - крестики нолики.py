from turtle import Screen, Turtle

# naught and cross functions

def cross():
    x, y = board.position()
    board.penup()
    board.setposition(x - 80, y - 80)
    board.pendown()
    board.setposition(x + 80, y + 80)
    board.penup()
    board.setx(x - 80)
    board.pendown()
    board.setposition(x + 80, y - 80)
    board.penup()
    board.home()

def naught():
    board.sety(board.ycor() - 80)
    board.pendown()
    board.circle(80)
    board.penup()
    board.home()

first_player = True

def choose():
    global first_player

    if first_player:
        naught()
    else:
        cross()

    first_player = not first_player

# movement
def move_left():
    x = board.xcor() - 200

    if x < -300:
        x = -200

    board.setx(x)

def move_right():
    x = board.xcor() + 200

    if x > 300:
        x = 200

    board.setx(x)

def move_down():
    y = board.ycor() - 200

    if y < -300:
        y = -200

    board.sety(y)

def move_up():
    y = board.ycor() + 200

    if y > 300:
        y = 200

    board.sety(y)

# screen

screen = Screen()
screen.bgcolor("black")
screen.title("tic tac toe")

# board

board = Turtle()
board.color("white")
board.speed('fastest')

# vertical lines
board.penup()
board.setposition(-100, -300)
board.pendown()
board.sety(300)
board.penup()
board.setx(100)
board.pendown()
board.sety(-300)
board.penup()

# horizontal lines
board.setposition(-300, 100)
board.pendown()
board.setx(300)
board.penup()
board.sety(-100)
board.pendown()
board.setx(-300)
board.penup()
board.home()

# Keybinding

screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")

screen.onkey(choose, "Return")

screen.listen()
screen.mainloop()
