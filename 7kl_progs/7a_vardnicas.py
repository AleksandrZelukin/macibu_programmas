vardnica = {}


while True:
    
    pilseta = input("Pilsēta: ")
    valsts = input("Valsts: ")
    vardnica[pilseta]=valsts
    if pilseta =="no":
        break

print(vardnica)
