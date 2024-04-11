# import turtle
# t = turtle.Pen()
import turtle
def draw_star(size, color):
    angle = 120
    turtle.fillcolor(color)
    turtle.begin_fill()

    for side in range(5):
        turtle.forward(size)
        turtle.right(angle)
        turtle.forward(size)
        turtle.right(72 - angle)
    turtle.end_fill()
    return

draw_star(50, "yellow")
turtle.mainloop()
