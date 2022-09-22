# Kevin Robbins
# Intro to CS
# 7/8/2020
# Python House Animation

# Allows the use of the Graphical User Interface (GUI)
#import simplegui
import random

# Handler to draw on canvas
def draw(canvas):
    #Draw one window based on coordinate arguments.
    def draw_window(x,y):
        canvas.draw_polygon([(x,y),(x+50,y),(x+50,y+50),(x,y+50)],3,"black","yellow")
        canvas.draw_line((x+25,y),(x+25,y+50),3,"black")
        canvas.draw_line((x,y+25),(x+50,y+25),3,"black")
        
    #Draw one white circle based on coordinate arguments.
    def draw_cloud(x,y):
        canvas.draw_circle((x,y), 20, 1, "white", "white")
        canvas.draw_circle((x+10,y+10), 15, 1, "white", "white")
        canvas.draw_circle((x+30,y+5), 20, 1, "white", "white")
        canvas.draw_circle((x+40,y+20), 15, 1, "white", "white")
        canvas.draw_circle((x+65,y+10), 20, 1, "white", "white")
        canvas.draw_circle((x+85,y+15), 15, 1, "white", "white")
        
    #Draw one mountain based on coordinate arguments. The color parameter is the fill color.
    def draw_mountain(x,y,color):
        canvas.draw_polygon([(x,y),(x+400,y+200),(x-400,y+200)],1,"brown",color)
    
    #Draw one tree based on coordinate arguments.
    def draw_tree(x,y,size):
        if (size=="l"):
            xa,ya,xb,yb,xc,yc,xd,yd,xe,ye,xf,yf=x+90,y+300,x-90,y+300,x-15,y+300,x+15,y+300,x+15,y+350,x-15,y+350
        elif (size=="m"):
            xa,ya,xb,yb,xc,yc,xd,yd,xe,ye,xf,yf=x+60,y+200,x-60,y+200,x-10,y+200,x+10,y+200,x+10,y+240,x-10,y+240
        else:
            xa,ya,xb,yb,xc,yc,xd,yd,xe,ye,xf,yf=x+30,y+100,x-30,y+100,x-5,y+100,x+5,y+100,x+5,y+130,x-5,y+130
        canvas.draw_polygon([(x,y),(xa,ya),(xb,yb)],1,"black","green")
        canvas.draw_polygon([(xc,yc),(xd,yd),(xe,ye),(xf,yf)],1,"black","brown")

    #Sun
    canvas.draw_circle((900,100), 50, 1, "orange", "gold")
    #Clouds
    draw_cloud(100,100)
    draw_cloud(150,120)
    draw_cloud(700,200)
    draw_cloud(750,175)
    #Mountains
    draw_mountain(1000,400,"rosybrown")
    draw_mountain(700,350,"tan")
    draw_mountain(500,400,"burlywood")
    draw_mountain(100,425,"sandybrown")
    #Yard
    canvas.draw_polygon([(0,500),(1000,500),(1000,700),(0,700)], 1, "black", "lightgreen")
    #Trees
    draw_tree(530,415,"s")
    draw_tree(600,400,"s")
    draw_tree(650,405,"s")
    draw_tree(825,355,"m")
    draw_tree(140,350,"m")
    draw_tree(900,325,"l")
    draw_tree(50,350,"l")
    #Roof
    canvas.draw_polygon([(300,250),(450,350),(150,350)], 1, "black", "saddlebrown")
    #House
    canvas.draw_polygon([(170,350),(430,350),(430,600),(170,600)], 1, "black", "lightyellow")
    #House addition
    canvas.draw_polygon([(430,450),(540,480),(430,480)],1,"black","saddlebrown")
    canvas.draw_polygon([(430,480),(520,480),(520,600),(430,600)],1,"black","lightyellow")
    #Windows
    draw_window(190,400)
    draw_window(275,400)
    draw_window(360,400)
    draw_window(360,500)
    draw_window(190,500)
    draw_window(450,500)
    #Front Door Transom
    canvas.draw_circle((300,500), 25, 3, "black", "yellow")
    canvas.draw_polyline([(288,479),(300,500),(312,479)], 3, "black")
    #Front Door
    canvas.draw_polygon([(275,500),(325,500),(325,600),(275,600)], 3, "black", "crimson")
    canvas.draw_circle((320,550), 4, 1, "black", "gold")
    
# Create a frame and assign callbacks to event handlers
#frame = simplegui.create_frame("Python House Animation", 1000, 700)
#frame.set_canvas_background("lightblue")
#frame.set_draw_handler(draw)

# Start the frame animation
#frame.start()
