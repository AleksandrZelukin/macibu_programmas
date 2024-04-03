import random
dators = random.randint(1,10)

lives = 3
while lives >0:
    speletajs = int(input("Ievadi skailis: "))
    if dators != speletajs:
        print("Nepaveicas...")
        lives = lives-1
        print(f"Tev palikā {lives} meģinājumus")
        if lives == 0:
            print(f"Dators uzminēja {dators}")
    else:
        print("Apsveicu! Tu esi uzvarejs!")
        break


