phonebook = {}
while True:
    jautajums = input("srtādajam? (y/n)\n")
    if jautajums == "y":
        vards = input("Vārds>> ")
        talrunis=input("Talrunis>> ")
        phonebook[vards]=talrunis
        print(phonebook)
    if jautajums == "n":
        print(phonebook)
        break
    if jautajums == "d":
        vards=input("tiek dzests vārds>> ")
        phonebook.pop(vards)
        print("ir dzests ierakst ar vārdu: ",vards)