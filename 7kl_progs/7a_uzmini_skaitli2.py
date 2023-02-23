from random import randrange

while True:
    player = int(input("Izvelies skaitli no 1 līdz 6>> "))
    dators = randrange(1,6,1)
    if player == dators:
        print("Tu uzvarejs!, dators ari uzminēja skaitli ",dators)
    else:
        print("Žel, dators uzvarejs!, viņš uzmineja skaitli ",dators)