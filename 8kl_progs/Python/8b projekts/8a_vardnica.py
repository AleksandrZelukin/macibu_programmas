book = {}
while True:
    jaut = input("Ievadisim klienta numuru? (y/n)")
    if jaut == "y":
        vards = input()
        talrunis = input()
        book[vards]=talrunis
        print(book)
    if jaut == "d":
        vards = input()
        book.pop(vards)
    if jaut == "n":
        print(book)
        break