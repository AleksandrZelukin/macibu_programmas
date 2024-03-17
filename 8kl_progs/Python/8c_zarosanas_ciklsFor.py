nauda = int(input("nauda>>"))
likme = 0.3
gadi = int(input("gadi>>"))

for i in range(gadi):
    nauda += nauda*(likme/100)
    print(round(nauda,2), "EUR")