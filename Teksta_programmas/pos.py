# import turtle package
import turtle 
  
# print position (by default)
# i.e; (0.0, 0.0)
print(turtle.pos())
  
# turtle move forward 
# by 40 pixels
turtle.forward(40)
  
# print position (after move)
# i.e; (150.0, 0.0)
print(turtle.position())
  
# turtle move forward by 40 pixels
# after taking right turn 
# by 45 degrees
turtle.right(45)
turtle.forward(40)
  
# print position
# (after next move) 
print(turtle.pos())
  
# turtle move forward by 80 
# pixels after taking left
# turn by 90 degrees
turtle.left(90)
turtle.forward(80)
  
# print position
# (after next move) 
print(turtle.pos())
  
# turtle move forward 
# by 40 pixels after taking 
# right turn by 90 degrees
turtle.right(90)
turtle.forward(40)
  
# print position (after next move) 
print(turtle.position())
  
# turtle move forward by 
# 40 pixels after taking 
# left turn by 45 degrees
turtle.left(45)
turtle.forward(40)
  
# print position 
# (after final move) 
print(turtle.pos())
