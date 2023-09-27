from turtle import *
up()
setposition(-100,-100)
down()
figura=int(textinput("title","Cik sturu figuru tu gribi?)"))
for i in range(figura):
    fd(200)
    lt(360/figura)
write('{}-sturis'.format(figura),font=('Arial',24,'italic'))
# write(figura,'-sturis',font=('Arial',24,'italic'))
done()