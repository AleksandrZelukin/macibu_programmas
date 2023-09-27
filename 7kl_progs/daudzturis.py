from turtle import *
fillcolor('yellow')
pencolor('yellow')
screensize(bg='blue')
speed(100)
figura=int(textinput('Figura?', 'cik sturi?'))

for i in range(figura):
    fd(150)
    lt(360/figura)

done()