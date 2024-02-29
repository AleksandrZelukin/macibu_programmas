import turtle

# Создаем экран
screen = turtle.Screen()
screen.title("Смайлик")

# Создаем черепаху
smiley = turtle.Turtle()

# Настройки для черепахи
smiley.width(4)
smiley.speed(5)

# Функция для рисования круга
def draw_circle(color, radius, x, y):
    smiley.penup()
    smiley.fillcolor(color)
    smiley.goto(x, y)
    smiley.pendown()
    smiley.begin_fill()
    smiley.circle(radius)
    smiley.end_fill()

# Главная часть смайлика (желтый круг)
draw_circle("yellow", 100, 0, -40)

# Рисуем глаза (круги)
draw_circle("white", 15, -35, 60)
draw_circle("white", 15, 35, 60)

# Рисуем зрачки (круги)
draw_circle("black", 7, -35, 60)
draw_circle("black", 7, 35, 60)

# Рисуем рот (полуовал)
smiley.penup()
smiley.goto(-40, 0)
smiley.pendown()
smiley.width(5)
smiley.right(90)
smiley.circle(40, -180)

# Завершаем работу
smiley.hideturtle()
screen.mainloop()
