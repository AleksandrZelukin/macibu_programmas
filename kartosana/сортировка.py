#Стандартная сортировка
a = [3, 2, 5 ,4, 7, 1]
a = sorted(a)
 
print(a) # [1, 2, 3, 4, 5, 7]


# Сортируем кортеж.
t = ('Zane', 'Bob', 'Janet')
t = sorted(t)
 
print(t) # ['Bob', 'Janet', 'Zane']

# Сортировка словаря.

d = {1:'a', 2:'b', 3:'c'}
d = sorted(d)
print(d) # [1, 2, 3]

# Обратная сортировка
data = [3, 2, 5 ,4, 7, 1]
a = sorted(data, reverse = True)
print(a) # [7, 5, 4, 3, 2, 1]
 
data = ('Zane', 'Bob', 'Janet')
b = sorted(data, reverse = True)
print(b) # ['Zane', 'Janet', 'Bob']


