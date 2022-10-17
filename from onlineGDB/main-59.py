x=int('z',36)
print(x)

print(oct(11011))
#схема Гернера - преобразование систем счисления
base = 7
x=int(input())
while x>0:
    digit = x%base
    print(digit, end='') #взять последнюю цифру
    x //= base #убрать последнюю цифру