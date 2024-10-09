'''
Kārlis noperka M kg ābolu maksājot C centus par kg. 
Cik centus X ir jāsamaksa par pirkumu? 
Cik atlikuma centus S viņš dabūs no L eiro?

L = int(input("Man kabatā ir: "))
C = float(input("Aboli maksa: "))
M = int(input("Grību pirkt(kg.): "))

S = L - (M*C)

print("Atlikums bus: ",S)

Annai ir a gadi, bet Marutai - m gadi. Kura no viņam ir vecāka?






Programma pieprasa kvadrāta mālu a un izskaitļo perimetru

Pļavā rotaļājas bērni un suņi. 
Zinot galvu un kāju kopējo skaitu (g un k), 
atrast, cik bērnu un cik suņu ir pļavā (b un s).
'''

cena = float(input("cena par kg: "))
nauda = float(input("cik man ir nauda: "))
svars = int(input("Cik pirku abolus: "))

kopa = svars * cena
atlikums = nauda - kopa

print("atlikums: ", atlikums)

a = int(input("kvadrata mala: "))
print("perimetrs kavadrata ir: ",a*4)