from turtle import *
#a=Turtle()
#a.screen.setup(800,800)


'''
n = 12
for z in range(n):
    fd(200)
    
    lt(180)
    
    rt(360/n)
'''
def mn(n):
    for z in range(n):
        fd(200/n)
        rt(360/n)
    
n = 8
for z in range(n):
    mn(n)
    rt(360/n)

