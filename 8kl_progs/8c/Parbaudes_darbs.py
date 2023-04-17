from turtle import *

a=int(textinput("Trijstrūis", "malas garums"))
h=int(textinput("Trijstrūis", "augstums"))

for i in range (3):
    fd(150)
    lt(360/3)
s = a*h/2    
write("Trijstūra laukums ir {} ".format(s), font=("Arial","24"))   
up()
goto(-150,-100)
down()
r=int(textinput("Aplis", "Radius"))

circle(r)
l = 2*r*3.14
write("Riņķa līnijas garums ir {} ".format(l),font=("Arial","24"))   




done()


