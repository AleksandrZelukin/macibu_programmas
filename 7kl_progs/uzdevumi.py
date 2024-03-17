# https://tproger.ru/problems/python-3-exercises-for-beginners-geekbrains/
# Сложите цифры целого числа.
def sum_digits(num):
    digits = [int(d) for d in str(num)]
    return sum(digits)

print(sum_digits(5245))

# Посчитайте, сколько раз символ встречается в строке.
string = 'Python Software Foundation'
string.count('o')

# Поменяйте значения переменных местами.
x = 5
y = 10
temp = x
x = y
y = temp
# 2
x = 5
y = 10
x, y = y, x

# Выведите первый и последний элемент списка.
lst = [1, 2, 3, 4, 5]
print(f'Первый: {lst[0]}; последний: {lst[-1]}')

# Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.
def convert(seconds):
    days = seconds // (24 * 3600)
    seconds %= 24 * 3600
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    print(f'{days}:{hours}:{minutes}:{seconds}')

convert(1234565)
