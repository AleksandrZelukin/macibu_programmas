#https://geekstand.top/development/grafika-v-python-pri-pomoshhi-modulja-turtle/
import turtle

a = turtle.Turtle()
window = turtle.Screen()

window.bgcolor("black")


#def polygon(n, size=80):
#    if n > 2:
#       angle = 360 / n
#
#        for n in range(0, n):
#            a.left(angle)
#           a.forward(size)



def polygon(n, size=80):
    if n > 2:
        angle = 360 / n
 
        for n in range(0, n):
            a.color(colors[n % 5])
            a.left(angle)
            a.forward(size)
a.speed(100)

colors = ['orange', 'cyan', 'blue', 'green', 'red']

size = 40

for i in range(0, 60):
    a.color(colors[i % 5])
    polygon(4, size)
    a.left(5)
    size = size + 3

window.mainloop()
