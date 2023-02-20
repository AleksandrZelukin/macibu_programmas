nauda1 = int(input("Nauda>> "))
likme = float(input("Banka likme>> "))
gads = int(input("Kopā gadus>> "))
nauda2 = int(input("Velama nauda>> "))

# while nauda2 > nauda1:
#     nauda1 +=nauda1*(likme/100)
#     gads +=1

# print(gads)

while nauda2 < nauda1:
    nauda1 =+ nauda1*(likme/100)
    gads -=1
    print(nauda1)

