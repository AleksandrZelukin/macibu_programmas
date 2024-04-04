import random
saraksts = ["akmens","šķēres","pāpirs"]

dators = random.choice(saraksts)
lives = 3
speletajs = input("Tavs variants?(akmens,šķēres,pāpirs) ")

if (dators == "akmens" and speletajs == "akmens") or\
    (dators == "šķēres" and speletajs == "šķēres") or\
    (dators == "pāpirs" and speletajs == "pāpirs"):
    print("neizšķirts")
elif (dators == "akmens" and speletajs == "šķēres") or\
    (dators == "šķēres" and speletajs == "pāpirs"):
    print("Dators uzvaretajs!")
elif (speletajs == "akmens" and dators == "šķēres") or\
    (speletajs == "šķēres" and dators == "pāpirs"):
    print("Jūs esat uzvaretajs!")