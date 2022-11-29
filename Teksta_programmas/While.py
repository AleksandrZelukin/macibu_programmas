print("Cikla while izmatošanas piemers")
print("Izvelēs saivenojumu vedids:\nparalelais nospiež 1, virknes - 2\n")
while True:
    y = int(input())
    if y == 1:
        print("Paralelais savienojums")
    if y == 2:
        print("virknes savienojums")
        
    if y >= 3:
        print("nepareizi dati!")
        break
        