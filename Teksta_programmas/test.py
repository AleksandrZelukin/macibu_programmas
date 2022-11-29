import math

print("Выберите фигуру: ")
print("1 - квадрат")
print("2 - круг")
print("3 - треугольник")
tip = str(input("Выбрано: "))
if tip == "1":
    a = float(input("Введите сторону а = "))
    s = a**2
elif tip == "2":
    r = float(input("Введите радиус r = "))
    s = math.pi*(r**2)
elif tip == "3":
    a = float(input("Введите сторону а = "))
    h = float(input("Введите сторону h = "))
    s = 0.5*a*h
else:
    print("Такой фигуры нету в списке.") 
    print("Выбирете другую фигуру")
print("Площадь: ", s)