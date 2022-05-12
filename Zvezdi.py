import turtle, random

dog = turtle.Turtle()
dog.speed(100)
okno = turtle.Screen()
okno.setup(800, 600)  # Устанавливаем размер окна
okno.bgcolor('darkblue')  # Делаем цвет неба
dog.hideturtle()  # убираем видимость курсора

def star(n, dlina, col):
    dog.begin_fill()  # Начало функции заливки
    if n % 2 != 0:  # Проверяем на четность
        for i in range(n):
            dog.color(col)  # Цвет нашей звезды
            dog.forward(dlina)
            y = n // 2 * 360 / n  # Формула расчета угла
            dog.left(y)
    else:
        n = n + 1  # Если количество вершин было четное, прибавляем 1
        star(n, dlina, col)  # Вызываем нашу функцию
    dog.end_fill()  # Конец функции заливки

for i in range (150):
    x = random.randint(-350, 350)  # Случайные координаты по х
    y = random.randint(-250, 250)  # Случайные координаты по у
    dog.up() # Поднимаем карандаш
    dog.setposition (x,y)# Перемещаемся по координатам
    dog.down()# Опускаем карандаш
    size = random.randint (10, 30) # Случайный размер от 10 до 30
    ver = random.randint (5, 15) # Случайное кол-во вершин от 5 до 15

    star(ver, size, 'yellow')  # При вызове функции передаем еще один аргумент, ЦВЕТ

turtle.mainloop()
