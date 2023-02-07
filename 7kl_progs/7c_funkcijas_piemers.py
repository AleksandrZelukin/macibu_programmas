def krajums(nauda, gads=1, likme=0.3):
    for i in range(gads):
        nauda += nauda*(likme/100)
        gads += 1
    print(round(nauda, 2))

p = krajums(1000,10, 0.25)

