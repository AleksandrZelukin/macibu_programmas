import random
saraksts = ["akmens","šķēres","papīrs"]
#random.shuffle(saraksts)
#print(saraksts[0])
dators = random.choice(saraksts)
speletajs = input("Jūsu izvēlē\n(akmens,šķēres,papīrs): ")

if dators == speletajs:
    print("neizšķirts")
if dators == "akmens" and speletajs == "šķēres":
    print("dators uzvareja")
if dators == "šķēres" and speletajs == "papīrs":
    print("dators uzvareja")
if dators == "papīrs" and speletajs == "akmens":
    print("dators uzvareja")
    
if speletajs == "akmens" and dators == "šķēres":
    print("Tu uzvareji")
    print(f"Dators izvēlējās {dators}")
if speletajs == "šķēres" and dators == "papīrs":
    print("Tu uzvareji")
    print(f"Dators izvēlējās {dators}")
if speletajs == "papīrs" and dators == "akmens":
    print("Tu uzvareji")
    print(f"Dators izvēlējās {dators}")