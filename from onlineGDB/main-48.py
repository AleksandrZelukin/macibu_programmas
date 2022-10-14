summa = float(input("Cik naudu tev ir? "))
summa2 = float(input("Cik tu grībi? "))
procent = float(input("Gadā Procentu likme: "))
count = 0 

while summa < summa2:
    summa += summa*(procent/100) 
    count += 1 
    print(count," gads",round(summa,2))

while True:
    if summa < summa2:
        summa += summa*(procent/100) 
        count += 1 
    else:
        print(count," gads",round(summa,2))
        break
   
summa = float(input("Cik tev ir? "))
procent = float(input("Gadā Procentu likme: "))
count = int(input("Uz cik gādu iebāzt? " )) 

for i in range (count):
    summa += summa*(procent/100)
    count += -1
    print(count," gads ",round(summa,2))



