def banka(nauda, likme, gadi):
   for i in range (gadi):
    nauda += nauda*(likme/100)
    gadi += -1
    print(gadi," gads ",round(nauda,2))


x = 1000
y = 0.3
z = 10

c = banka(x,y,z)
print(c)