def krajums(nauda, gads=1, likme=0.03):
    for i in range(gads):
        nauda += nauda*(likme/100)
        gads += 1
    print(round(nauda, 2))


a = int(input("Summa: "))
g = int(input("Termiņš: "))
p = krajums(a,10, 0.25)

