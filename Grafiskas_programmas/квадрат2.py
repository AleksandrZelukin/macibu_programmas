from turtle import *
color('red', 'yellow')
begin_fill()


while True:
       #goto(-100,100)
       forward(200)
       left(90)
       if abs(pos()) < 1:
              break
end_fill()
done()
