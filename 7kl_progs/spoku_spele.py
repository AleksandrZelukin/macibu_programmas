from random import randint
punkti = 0
spele = {}

while True:
    jautajums=input("Spēlejam?>> ")
    if jautajums == "y":
        vards=input("Tavs vārds >>")
        while True:
            durvis=int(input("Kads durvis?>> "))
            spoks=randint(1,3)
            if durvis != spoks:
                punkti +=1
                print("Spoka šeit nav, tu dabuj ",punkti,"punktus")
            else:
                print("Spoks!")  
                print("Spēle beidzas un tu kopa saņem ",punkti,"punktus")
                spele[vards]=punkti
                print(spele)
                punkti = 0
                break 
    if jautajums == "n":
        print(spele)
        break

