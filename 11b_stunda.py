from turtle import *
b = Turtle()
b.screen.setup(550,550)
b.shape("turtle")
b.up()
b.goto(-250,250)
b.fillcolor("lightblue")
b.begin_fill()
b.down()
b.forward(500)
b.right(90)
b.forward(500)
b.right(90)
b.forward(500)
b.right(90)
b.forward(500)
b.end_fill()

b.up()
b.goto(250,0)
b.fillcolor("blue")
b.begin_fill()
b.down()
b.circle(250)
b.end_fill()




b.screen.exitonclick()
b.screen.mainloop()
