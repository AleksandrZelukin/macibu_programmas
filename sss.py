
x=float(input("Введите длину стороны квадрата: "))
print(x*4, ' - периметр квадрата')

b=float(input("Введите первую оценку:"))
с=float(input("Введите вторую оценку:"))
d=float(input("Введите третью оценку:"))
print((b+с+d)/3, " - средняя арифметическая")

e=float(input("Сколько киллограмов яблок купил Карлис?"))
f=float(input("Сколько центов стоил киллограм яблок?"))
g=float(input("Сколько евро было у Карлиса?"))
print(g-(e*f)," - сколько осталось денег у Карлиса")


ages = []
names = ["Aнна", "Марута"]
for name in names:
    ages.append(int(input("Возраст {}а: ".format(name))))
j = 0
M = []
m = max(ages)
for age in ages:
    if age == m:
        M.append(j)
    j += 1
if len(M) == 1:
    print("{} старше всех.".format(names[M[0]]))
elif len(M) == 2:
    for i, v in enumerate(names):
        if i not in M:
            young = v
            print("{} и {} старше {}а.".format(names[M[0]], names[M[1]], young))

