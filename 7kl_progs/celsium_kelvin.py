print("Ko daram?")
print( """
        Celsius to Fahrenheit -1
        Fahrenheit to Celsius -2
        Celsius to Kelvin -3
        Kelvin to Celsius -4
        Kelvin to Fahrenheit -5
        Fahrenheit to Kelvin -6""")

izvele = input()
if izvele == "1":
    print("Celsius to Fahrenheit:")
    c = int(input())
    f = c*(9/5)+32
    print(f)
if izvele == "2":
    print("Fahrenheit to Celsius:")
    f = int(input())
    c = (f-32)*(5/9)
    print(c)
if izvele == "3":
    print("Celsius to Kelvin:")
    c = int(input())
    k = c+273.15
    print(k)
if izvele == "4":
    print("Kelvin to Celsius :")
    k = int(input()) 
    c = k-273.15
    print(c)
if izvele == "5":
    print("Kelvin to Fahrenheit :")
    k = int(input()) 
    f = k-273.15*9/5+32
    print(f)
if izvele == "6":
    print("Fahrenheit to Kelvin :")
    f = int(input()) 
    k = (f-32)*5/9+273.15
    print(f)