from turtle import *

a=int(textinput("Tristruis", "Pamatne"))
h=int(textinput("Tristruis", "Augstums"))

for i in range (3):
    fd(150)
    lt(360/3)
write(a*h,font=("Arial","24"))   
up()
goto(-150,0)
down()
r=int(textinput("Aplis", "Radius"))

circle(r)
write(2*r*3.14,font=("Arial","24"))   




done()


