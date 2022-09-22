from tkinter import *
def keyPressHandler(event):
    print(event.char, 'код =', event.keycode)
class MyLine:
    def __init__(self, line_id, start_x, start_y):
        self._id = line_id
        self._start_x = start_x
        self._start_y = start_y
lineUnderCreation = None
def mouseButton1PressHandler(event):
    #создаём новую линию
    global lineUnderCreation
    canv = event.widget
    line_id = canv.create_line(event.x, event.y, event.x, event.y)
    lineUnderCreation = MyLine(line_id, event.x, event.y)
def mouseButton1ReleaseHandler(event):
    global lineUnderCreation
    lineUnderCreation = None
def mouseMotionHandler(event):
    canv = event.widget
    if event.state == 256:
        #зажата левая кнопка мышки - меняем создаваемую линию
        canv.delete(lineUnderCreation._id)
        line_id = canv.create_line(lineUnderCreation._start_x,
                                   lineUnderCreation._start_y,
                                   event.x, event.y)
        lineUnderCreation._id = line_id
        
root = Tk()
mainFrame = Frame(root)
canv = Canvas(mainFrame, bg = 'white', cursor = 'pencil')
canv["width"] = 600
canv["height"] = 600
canv.bind("<KeyPress>", keyPressHandler)
canv.bind("<Motion>", mouseMotionHandler)
canv.bind("<Button-1>", mouseButton1PressHandler)
#canv.bind("<Button-1>", mouseButton1ReleaseHandler)
canv.pack()
mainFrame.pack()
canv.focus()
root.mainloop()
