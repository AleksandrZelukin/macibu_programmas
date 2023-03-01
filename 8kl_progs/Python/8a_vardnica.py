book = {}
while True:
    jautajums = input("""
    ==========================
    Lai ievadit jaunu ierakstu
    nospiež 1
    iziet - 2
    dzest ierakstu - 3
    ==========================
    """
    )
    if jautajums == "1":
        vards=input("Vārds>>")
        talrunis=input("Talruna numurs>>")
        book[vards]=talrunis
        print(book)
    if jautajums == "3":
        vards=input("Vārds>>")
        book.pop(vards)
        print(book)
    if jautajums == "2":
        print(book)
        break