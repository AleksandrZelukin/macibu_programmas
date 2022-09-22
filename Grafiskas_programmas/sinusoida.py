
import tkinter
import math

# Пользовательские процедуры
def plot_x_axe(x0,y0,x1):
    x_axe=[]
    xx=(x0,y0)
    x_axe.append(xx)
    xx=(x1,y0)
    x_axe.append(xx)
    canvas.create_line(x_axe,fill="black",width=2)

def plot_y_axe(x0,y0,y1):
    y_axe=[]
    yy=(x0,y1)
    y_axe.append(yy)
    yy=(x0,y0)
    y_axe.append(yy)
    canvas.create_line(y_axe,fill="black",width=2)

def plot_func0(x0,x1,dx,y0,y1):
    x0i=int(x0)
    x1i=int(x1)
    y0i=int(y0)
    y1i=int(y1)
    a=y1
    b=(y0 - y1)/(x1-x0)
    points=[]
    for x in range(x0i,x1i,dx):
        y=int(a+b*x)
        pp=(x,y)
        points.append(pp)
    
    canvas.create_line(points,fill="blue",smooth=1)
    plot_y_axe(x0i,y0i,y1i)
    plot_x_axe(x0i,y0i,x1i)

def plot_func1(x0,x1,dx,y0,y1):
    x0i=int(x0)
    x1i=int(x1)
    y0i=int(y0)
    y1i=int(y1)
    a=y0
    b=y0-y1
    points=[]
    for x in range(x0i,x1i,dx):
        y=int(a-y1i*b/x)
        pp=(x,y)
        points.append(pp)
        
    canvas.create_line(points,fill="blue",smooth=1)
    plot_y_axe(x0i,y0i,y1i)
    plot_x_axe(x0i,y0i,x1i)

def plot_func2(x0,x1,dx,y0,y1):
    x0i=int(x0)
    x1i=int(x1)
    y0i=int(y0)
    y1i=int(y1)
    a=(y0-y1)/(15*x1)
    b=1+((y0-y1)/(x1-x0))
    points=[]

    for x in range(x0i,x1i,dx):
        y=y0i-int(a*(x-x0i)**b)
        pp=(x,y)
        points.append(pp)
    
    canvas.create_line(points,fill="blue",smooth=1)
    plot_y_axe(x0i,y0i,y1i)
    plot_x_axe(x0i,y0i,x1i)

def plot_func3(x0,x1,dx,y0,y1):
    x0i=int(x0)
    x1i=int(x1)
    y0i=int(y0)
    y1i=int(y1)
    ay=150
    y0i=150
    points=[]
    for x in range(x0i,x1i,dx):
        y=y0i-ay*math.cos(x*dx)
        pp=(x,y)
        points.append(pp)
 
    canvas.create_line(points,fill="blue",smooth=1)
    plot_y_axe(x0i,0,y0i+ay)
    plot_x_axe(x0i,y0i,x1i)
#

def DrawGraph():
    fn=func.get()
    f=fn[0]
    x0=50.0
    y0=250.0
    x1=450.0
    y1=50.0
    dx=10

    if f=="0":
        canvas.delete("all")
        plot_func0(x0,x1,dx,y0,y1)
    elif f=="1":
        canvas.delete("all")
        plot_func1(x0,x1,dx,y0,y1)
    elif f=="2":
        canvas.delete("all")
        plot_func2(x0,x1,dx,y0,y1)
    else:
        canvas.delete("all")
        plot_func3(x0,x1,dx,y0,y1)

# Основная часть

tk=tkinter.Tk()


tk.title("Sample")
# Верхняя часть окна со списком и кнопками
menuframe=tkinter.Frame(tk)
menuframe.pack({"side":"top","fill":"x"})
# Надпись для списка
lbl=tkinter.Label(menuframe)
lbl["text"]="Выбор:"
lbl.pack({"side":"left"})

# Инициализация и формирования списка
func=tkinter.StringVar(tk)
func.set('0 y=Ax+B')
#
fspis=tkinter.OptionMenu(menuframe,func,
    '0 y=Ax+B',
    '1 y=A+B/x',
    '2 y=Ax^B',
    '3 y=A*cos(Bx)')
fspis.pack({"side":"left"})

# Кнопка управления рисованием
btnOk=tkinter.Button(menuframe)
btnOk["text"]="Нарисовать"
btnOk["command"]=DrawGraph
btnOk.pack({"side":"left"})

# Кнопка закрытия приложения
button=tkinter.Button(menuframe)
button["text"]="Закрыть"
button["command"]=tk.quit
button.pack({"side":"right"})

# Область рисования (холст)
canvas=tkinter.Canvas(tk)
canvas["height"]=360
canvas["width"]=480
canvas["background"]="#eeeeff"
canvas["borderwidth"]=2
canvas.pack({"side":"bottom"})

tk.mainloop()

