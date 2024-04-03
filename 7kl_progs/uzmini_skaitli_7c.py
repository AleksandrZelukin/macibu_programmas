import random
dators = random.randint(1,10)
lives = 3
while lives >0:
    speletajs = int(input("Ievadi skairlis: "))
    if dators != speletajs:
        print("Tu esi zaudējs")
        if dators < speletajs:
            print("Dators uzmnēja skaitlis mazak, neka tu ievādi!")
        lives = lives-1
    else:
        print(f"Dators āri uzmineja skaitis {dators},Tu esi uzvarejs!")
        break
        