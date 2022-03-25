import turtle

def show_cat():
    turtle.ht()
    turtle.penup()
    turtle.goto (15, 220)
    turtle.color("black")
    turtle.write("CAT", move=False, align="center", font=("Times New Roman", 120, "bold"))

def check_button(x, y):
    if -300 < x < 300 and 200 < y < 400:
        show_cat()

screen = turtle.Screen()
screen.setup(800,800)

turtle.penup()
turtle.goto(-300, 200)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor('red')
turtle.fd(600)
turtle.left(90)
turtle.fd(300)
turtle.left(90)
turtle.fd(600)
turtle.left(90)
turtle.fd(300)
turtle.left(90)
turtle.end_fill()

turtle.onscreenclick(check_button)

turtle.mainloop()
