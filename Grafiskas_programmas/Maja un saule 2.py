from turtle import *
c=Turtle()
c.screen.setup(800,900)
#Maja
c.fillcolor("blue")
c.up()
c.goto(-200,-400)
c.begin_fill()
c.down()
c.goto(200,-400)
c.goto(200,-200)
c.goto(-200,-200)
c.goto(-200,-400)
c.end_fill()
#Jumta
c.up()
c.fillcolor("red")
c.begin_fill()
c.goto(-250,-200)
c.down()
c.goto(0,-100)
c.goto(250,-200)
c.goto(-250,-200)
c.end_fill()


#Logs
c.up()
c.fillcolor("lightblue")
c.goto(-50,-220)
c.down()
c.begin_fill()
c.forward(100)
c.right(90)
c.forward(100)
c.right(90)
c.forward(100)
c.right(90)
c.forward(100)
c.end_fill()

#text
c.up()
c.goto(-30,-270)

c.write("Sveiki!", font=("Arial",15, "bold"))


#stari

c.fillcolor( 'yellow')
begin_fill()
c.goto(-200,150)
c.down()
n=24
for i in range(n):
    c.forward(200)
    c.left(180)
    c.left(360/n)

end_fill()



c.screen.exitonclick()
