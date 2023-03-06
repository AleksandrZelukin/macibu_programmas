from random import randint
l = 1
punkti = 0
spele = {}
while True:
    jautajums=("Spelejam? y/n")
    if jautajums =="y":
        vards=input("Tavs vārds>> ")
        doors=int(input("kads durvis?>>"))
        spoks=randint(1,3)
        if doors == spoks:
            print("Spoks!")
            l -=1
            print("Spēles beigas!")
            spele[vards]=punkti
        else:
            print('Spoka nav!')
            print('Tu vari ienākt nākamajā istabā.')
            punkti +=1
            print("Tu dabuj ",punkti,"punktus")
            
    if jautajums =="n":
        print(spele)
        break
