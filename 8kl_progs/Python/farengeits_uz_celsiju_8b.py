f = input("Temperatura Farengeita: ")
f = float(f)
c = round(((f-32)/1.8),1)
print("Temperatura Celsijos bus: ",c)

c = input("Temperatura Celsijos: ")
c = float(c)
f = round((c*1.8)+32)
print("Temperatura Farengeita bus: ",f)
