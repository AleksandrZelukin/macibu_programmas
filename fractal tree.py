import turtle

h = turtle.Turtle(shape="turtle")
b = turtle.Screen()
b.screensize(1080,1920)
b.setup(width = 1.0, height = 1.0)
b.bgcolor("black")
h.left(90)

h.speed()
h.pensize(3)
h.color("brown")

h.speed(0)


def tree(i):
    if i < 10:
        return

    else:
        h.forward(i)
        h.color("orange")
        h.circle(2)
        h.color("brown")
        h.left(30)
        tree(3 * i / 4)
        h.right(60)
        tree(3 * i / 4)
        h.left(30)
        if i == 100:
            h.color("brown")
        else:
            h.color("brown")
        h.backward(i)



tree(100)

turtle.done()
