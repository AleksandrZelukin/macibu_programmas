from turtle import *
t = Turtle()
t.screen.setup(800, 800)
def flower(x, y, color):
    t.up()
    t.goto(x, y - 200)
    t.setheading(90)
    t.color("green")
    t.down()
    t.fd(200)
    t.setheading(0)
    t.color("yellow")
    t.begin_fill()
    t.circle(20, 360)
    t.end_fill()
    for i in range(4):
        t.color(color)
        t.begin_fill()
        t.circle(-35, 360)
        t.end_fill()
        t.color("yellow")
        t.circle(20, 90)
t.speed(0) 
flower(-250, 250, "red")
flower(200, -200, "blue")
flower(100, 100, "green")
flower(-100, 100, "cyan")
flower(-200, -200, "purple")
t.screen.exitonclick()
t.screen.mainloop()
