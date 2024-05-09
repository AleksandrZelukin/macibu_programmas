from turtle import *
speed(1000)
def kegelis (x,y):
    for m in range (24):
        y += 30
        if m% 2 == 0:
            x = -425
        else:
            x = -450
            
        for k in range(16):
            up()
            setposition(x,y)
            down()   
            for i in range(2):
                fd(50)
                rt(90)
                fd(25)
                rt(90)
            x += 55    
    
            
        
kegelis(-450,-370)
done()