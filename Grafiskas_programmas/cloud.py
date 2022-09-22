from processing import *
from random import randint

def drawCloud(): 
    for i in range(1,16):  
        size=randint(20,70)
        xOffset=randint(-40,40)
        yOffset=randint(-30,30)
        ellipse(100+xOffset,100+yOffset,size,size)
   
def setup():
    strokeWeight(12)
    size(200,200)
    background(111,170,252)
    fill(255,255,255)
    stroke(255,255,255)    
    drawCloud()

run()
