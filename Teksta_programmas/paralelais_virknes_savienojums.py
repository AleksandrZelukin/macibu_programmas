print("Cikla while izmatošanas piemers")
print("Izvelēs saivenojumu vedids:\nparalelais nospiež 1, virknes - 2\n")
while True:
    y = int(input())
    if y == 1:
        print("Paralelais savienojums")
        print("Cik rezistoru ir ķēdē? max=5")
        count=int(input())
        if count == 2:
            r1=float(input("R1="))
            r2=float(input("R2="))
            r=round(1/(1/r1+1/r2),2)
            print("R= ",r,"Ohm")

        if count == 3:
            r1=float(input("R1="))
            r2=float(input("R2="))
            r3=float(input("R3="))
            r=round(1/(1/r1+1/r2+1/r3),2)
            print("R= ",r,"Ohm")


        if count == 4:
            r1=float(input("R1="))
            r2=float(input("R2="))
            r3=float(input("R3="))
            r4=float(input("R4="))
            r=round(1/(1/r1+1/r2+1/r3+1/r4),2)
            print("R= ",r,"Ohm")

        if count == 5:
            r1=float(input("R1="))
            r2=float(input("R2="))
            r3=float(input("R3="))
            r4=float(input("R4="))
            r5=float(input("R5="))
            r=round(1/(1/r1+1/r2+1/r3+1/r4+1/r5),2)
            print("R= ",r,"Ohm")
    if y == 2:
        print("virknes savienojums")
        
        print("Cik rezistoru ir ķēdē? max=5")
        count=int(input())
        if count == 2:
            r1=float(input("R1="))
            r2=float(input("R2="))
            r=round(r1+r2,2)
            print("R= ",r,"Ohm")

        if count == 3:
            r1=float(input("R1="))
            r2=float(input("R2="))
            r3=float(input("R3="))
            r=round(r1+r2+r3,2)
            print("R= ",r,"Ohm")


        if count == 4:
            r1=float(input("R1="))
            r2=float(input("R2="))
            r3=float(input("R3="))
            r4=float(input("R4="))
            r=round(r1+r2+r3+r4,2)
            print("R= ",r,"Ohm")

        if count == 5:
            r1=float(input("R1="))
            r2=float(input("R2="))
            r3=float(input("R3="))
            r4=float(input("R4="))
            r5=float(input("R5="))
            r=round(r1+r2+r3+r4+r5,2)
            print("R= ",r,"Ohm")
    if y >= 3:
        print("nepareizi dati!")
        break
