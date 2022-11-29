import math, os
while True:
    os.system("cls")
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
        listnumber = [3,4,5];
        print("Среднее арифмитическое = ", sum(listnumber) / len(listnumber))
        break
    elif tip == "":    
        # Подумать над этой задачи!
        m = int(input("Введите кг = "))
        с = int(input("Введите цены = "))
        print("Вова должен заплатить: ")
        break
    elif tip == "4":
        a = int(input("Введите длину куба = "))
        d = int(input("Введите диагональ куба = "))
        print("Объем куба: ", a*3)
        print("Площадь поверхности: ", 6*a**2)
        print("Диагональ куба: ", math.sqrt(d)*a)
        break
    elif tip == "": 
        # Подумать над этой задачи!
        g = int(input("Введите количество голов"))
        k = int(input("Введите количество ног"))
        print("Общее количество", g+k)
        print("")
        break
    else:
        print("Такое выбранного не существует!")



        