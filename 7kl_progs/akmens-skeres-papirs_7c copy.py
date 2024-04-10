import random
saraksts = ["akmens","šķēres","papīrs"]
dators = random.choice(saraksts)
lives = 3
datorwin = 0
youwin = 0
while lives > 0:
    speletajs = input("Jūsu izvēlē\n(akmens,šķēres,papīrs): ")

    if dators == speletajs:
        print("neizšķirts")
        lives -= 1
        print(f"Palikā {lives} meģinājums")
    if (dators == "akmens" and speletajs == "šķēres") or (dators == "šķēres" and speletajs == "papīrs") or (dators == "papīrs" and speletajs == "akmens"):
        print("dators uzvareja")
        lives -= 1
        datorwin +=1
        print(f"Palikā {lives} meģinājums")
    
    if (speletajs == "akmens" and dators == "šķēres") or (speletajs == "šķēres" and dators == "papīrs") or (speletajs == "papīrs" and dators == "akmens"):
        print("Tu uzvareji")
        lives -= 1
        youwin += 1
        print(f"Dators izvēlējās {dators}")
    
    
    print("Dators: ",datorwin)
    print("Jūs: ",youwin)