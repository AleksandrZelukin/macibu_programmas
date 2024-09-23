summa = int(input("Sakuma ielikums "))
likme = 0.03
termins = int(input("Cik gadu? "))
sakuma_term = 0
while sakuma_term < termins:
    sakuma_term +=1
    summa += summa*likme
print(round(summa,2))