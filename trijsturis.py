from turtle import *
a = Turtle()
a.screen.setup(800, 800)
def trijsturis(x,angle,color):
#    a.goto(-x,x)
    a.right(angle)
    a.fd(x)
    a.right(angle)
    a.fd(x)
    a.right(angle)
    a.fd(x)

trijsturis(200,120, "black")
trijsturis(150,120,"red")

a.screen.exitonclick()
a.screen.mainloop()
