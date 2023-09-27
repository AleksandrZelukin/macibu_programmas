def krajums(nauda, likme = 0.3, laiks=1):
    for i in range(laiks):
        nauda += nauda*(likme/100)
        laiks+=1
    print(round(nauda,2))

p = krajums(1000)