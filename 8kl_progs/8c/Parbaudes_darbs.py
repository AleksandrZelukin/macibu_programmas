from turtle import *
up()
goto(-100,300)
down()
write("Tainsstūra trijstūra lauku noteikšana", font=("Arial","24"))

up()
goto(0,0)
down()
a=int(textinput("Trijstrūis", "pirmais katetes"))
h=int(textinput("Trijstrūis", "otrais katets"))


fd(a)
lt(90)
fd(h)
goto(0,0)
# for i in range (3):
#     fd(150)
#     lt(360/3)
s = a*h/2    
write("Trijstūra laukums ir {} ".format(s), font=("Arial","24"))  

up()
goto(-100,200)
down()
write("Riņķa līnijas garuma noteikšana", font=("Arial","24"))

up()
goto(-150,-100)

down()
r=int(textinput("Aplis", "Radius"))

circle(r)
l = 2*r*3.14
write("Riņķa līnijas garums ir {} ".format(l),font=("Arial","24"))   




done()


