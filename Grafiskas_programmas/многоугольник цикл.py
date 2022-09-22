from turtle import*

def drawSunshine(im):
    draw = ImageDraw.Draw(im)
    x, y = im.size
    draw.ellipse((370,200, 400,230), fill='red',outline='black')
    draw.line((370,205,390,218), fill='black',width=3)
    draw.point((100,100),'red')
    im.show()
