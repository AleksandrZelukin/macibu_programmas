roman_numbers = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
                 'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
                 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}


def to_roman(number):
    roman = ''
    for letter, value in roman_numbers.items():
        while number >= value:
            roman += letter
            number -= value
    return roman


print("24 =", to_roman(24))


def arabic_to_roman(number):
    roman_numerals = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    result = ""

    for value, numeral in roman_numerals:
        while number >= value:
            result += numeral
            number -= value

    return result

print(arabic_to_roman(24))

rom_num = input()

print(rom_num, 'in arabic numbers')

alloc = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
}

k = len(rom_num)
arb_num = 0
pst_curr = 0
while k > 0:
    curr = alloc[rom_num[k-1]]
    if curr < pst_curr:
        curr = - curr
    arb_num = arb_num+curr
    k = k-1
    pst_curr = curr; del curr

del k; del pst_curr

print('equals to', arb_num, '.')