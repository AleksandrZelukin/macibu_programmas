from turtle import *
a=Turtle()
a.screen.setup(800,800)
a.screen.bgcolor("lightblue")

#SAULE
a.pencolor('yellow')
a.fillcolor("yellow")
a.begin_fill()
a.up()
a.goto(-150,200)
a.down()
a.circle(50)
a.end_fill()
a.up()

#Stāri
a.down()
a.pensize(4)
n=20 #Stāru daudzums - cikls

for i in range(n):
    a.goto(-150,250)
    a.forward(100)
    a.left(360/n)
a.up()
a.pencolor('black')

#Māja
a.goto(-200,-350)
a.down()
a.fillcolor("red")
a.begin_fill()
a.goto(200,-350)
a.goto(200,-200)
a.goto(-200,-200)
a.goto(-200,-350)
a.end_fill()
a.up()

#Jumta
a.goto(-250,-200)
a.down()
a.fillcolor("blue")
a.begin_fill()
a.goto(0,-100)
a.goto(250,-200)
a.goto(-250,-200)
a.end_fill()
a.up()

#Logs
a.goto(-50,-220)
a.down()
a.fillcolor("lightblue")
a.begin_fill()
for i in range(4):
    a.forward(75)
    a.right(90)
a.end_fill()
a.up()

a.goto(-150,0)
   
a.write("Sveicens no skolotāja!", font=("Arial", 25, "bold"))


a.screen.exitonclick()
