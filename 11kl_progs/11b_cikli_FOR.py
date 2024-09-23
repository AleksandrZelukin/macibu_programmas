summa = int(input("Sakuma ielikums "))
likme = 0.03
termins = int(input("Cik gadu? "))
for i in range(termins):
    summa += summa*likme
print(round (summa,2))