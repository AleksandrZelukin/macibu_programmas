phonebook = {}
while True:
    jautajums = input("srtādajam? (y/n/d/r)\n")
    if jautajums == "y":
        vards = input("Vārds>> ")
        talrunis=input("Talrunis>> ")
        phonebook[vards]=talrunis
        print(phonebook)
    if jautajums == "n":
        print(phonebook)
        f = open("bc_vardnicas.txt","a",encoding="utf-8")
        print(phonebook, file=f)
        f.close()
        break
    if jautajums == "d":
        vards=input("tiek dzests vārds>> ")
        phonebook.pop(vards)
        print("ir dzests ierakst ar vārdu: ",vards)
    if jautajums == "r":
        for i in  open("bc_vardnicas.txt","r",encoding="utf-8"):
            print(i)
    
    