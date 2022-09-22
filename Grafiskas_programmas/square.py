import turtle
a = turtle.Turtle()
a.shape("turtle")
for i in range(4):
    a.forward(100)
    a.right(90)
    


b = turtle.Turtle()
b.goto(-100,100)


b.shape("turtle")
for i in range(5):
    b.forward(100)
    b.right(144)

c = turtle.Turtle()
c.goto(-200,200)
c.shape("turtle")
# c.hideturtle()
for i in range(8):
    c.forward(100)
    c.right(135)


turtle.exitonclick()
