import math
while True:
    print("Выберите: ")
    print("1 - Периметр квадрата")
    print("2 - Среднее арифмитическое")
    print("3 - Задача про Вову")
    print("4 - Задача про куб")
    print("5 - Задача про детей и собак")
    tip = str(input("Выбрано: "))
    if tip == "1":
        s = int(input("Длина стороны квадрата = "))
        p = 4*s
        print("Периметр: ", p)
        break
    elif tip == "2":
        listnumber = [3, 4, 5]
        print(f"Среднее арифмитическое = {sum(listnumber) / len(listnumber)}")
        break
    elif tip == "3":
        l = float(input("Введите количество денег = "))
        m = float(input("Введите кг яблок = "))
        c = float(input("Введите центы за 1кг = "))
        x=m*c; print(f"Вы заплатили {x} евро")
        w=l-x; print(f"У вас осталось {w} евро")
        break
    elif tip == "4":
        a = int(input("Введите длину куба = "))
        d = int(input("Введите диагональ куба = "))
        print(f"Объем куба: {a*3}")
        print(f"Площадь поверхности: {6*a**2}")
        print(f"Диагональ куба: {math.sqrt(d)*a}")
        break
    elif tip == "5":
        g = int(input("Введите количество голов = "))
        k = int(input("Введите количество ног = "))
        b = int(input("Введите количество детей = "))
        s = int(input("Введите количество собак = "))
        print(f"Общее количество на поляне: {b+s}")
        print(f"Общее количество голов и ног: {g*k}")
        break
    else:
        print("Такое выбранного не существует!")
