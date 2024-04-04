from random import choice
saraksts = ["akmens","šķēres","papīrs"]
dators = choice(saraksts)
speletajs = input("akmens/šķēres/papīrs:")

if dators == speletajs:
    print("neizšķirts")
    print(f"Dators āri izvēlējās {dators}")
if (dators == "akmens") and (speletajs == "šķēres"):
    print(f"Dators izvēlējās {dators}")
    print("dators uzvareja")
if (dators == "šķēres") and (speletajs == "papīrs"):
    print("dators uzvareja")
    print(f"Dators izvēlējās {dators}")
if (dators == "papīrs") and (speletajs == "akmens"):
    print("dators uzvareja")
    print(f"Dators izvēlējās {dators}")
if (dators == "akmens") and (speletajs == "papīrs"):
    print("Tu uzvareji")
    print(f"Dators izvēlējās {dators}")
if (dators == "šķēres") and (speletajs == "akmens"):
    print("Tu uzvareji")
    print(f"Dators izvēlējās {dators}")
if (dators == "papīrs") and (speletajs == "šķēres"):
    print("Tu uzvareji")
    print(f"Dators izvēlējās {dators}")