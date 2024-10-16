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