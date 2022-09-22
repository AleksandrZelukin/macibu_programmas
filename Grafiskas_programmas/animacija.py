from graphics import *
import time
win = GraphWin("Окно для графики", 400, 400)
win.setBackground('white')
x = [10, 20, 30]
y = [100, 200, 300]
def car(x, y, color, flag): 
    body = Polygon(
        Point(x, y),
        Point(x, y - 10),
        Point(x + 10, y - 20),
        Point(x + 30, y - 20),
        Point(x + 40, y - 10),
        Point(x + 50, y - 10),
        Point(x + 50, y))
    wheel1 = Circle(Point(x + 8, y + 4), 4)
    wheel2 = Circle(Point(x + 42, y + 4), 4)
    window = Polygon(
        Point(x + 20, y - 12),
        Point(x + 20, y - 18),
        Point(x + 30, y - 18),
        Point(x + 36, y - 12))
    body.setOutline(color)
    body.setFill(color)
    wheel1.setFill("black")
    wheel2.setFill("black")   
    window.setOutline("cyan")
    window.setFill("cyan")
    
    if flag == 1:
       body.draw(win)
       wheel1.draw(win)
       wheel2.draw(win)
       window.draw(win)
       
    if flag == 0:
    
       body.setOutline('white')
       body.setFill('white')
       wheel1.setFill("white")
       wheel1.setOutline('white')
       wheel2.setFill("white") 
       wheel2.setOutline('white')
       window.setOutline("white")
       window.setFill("white")     
       body.draw(win)
       wheel1.draw(win)
       wheel2.draw(win)
       window.draw(win)

for i in range(20):
    car(x[0], y[0], 'green', 1)
    car(x[1], y[1], 'green', 1)
    car(x[2], y[2], 'green', 1)
  
    time.sleep(1)
    car(x[0], y[0], 'green', 0)
    car(x[1], y[1], 'green', 0)
    car(x[2], y[2], 'green', 0)
    x[0] += 10
    x[1] += 10
    x[2] += 10
win.getMouse()
win.close()
