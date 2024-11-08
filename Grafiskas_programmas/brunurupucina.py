from turtle import *
n = 1
up()
goto(200,0)
down()
for i in range(n):
    forward(50/n*4)
    left(360/n)

mainloop()