'''
1.Programma pieprasa kvadrāta mālu a un izskaitļo perimetru

2.Programma pieprasa Kārļa trīs atzīmes un izskaitļo 
vidējo aritmētisko.

3.Kārlis nopirka M kg abolu maksājot C centus par kg. 
Cik centus X ir jāsamaksa par pirkumu? 
Cik atlikuma centus S viņš dabūs no L eiro?

Annai ir a gadi, bet Marutai - m gadi. Kas no viņam ir vecāka?

Pļavā rotaļājas bērni un suņi. 
Zinot galvu un kāju kopējo skaitu (g un k), 
atrast, cik bērnu un cik suņu ir pļavā (b un s).

'''
atzime1 = int(input())
atzime2 =int(input())
atzime3 =int(input())
videja_atzime= (atzime1+atzime2+atzime3)/3
print("Vidēja atzime Karļim ir: ", videja_atzime)

side = int(input("Kvadrata māla: "))
p = side*4
print("Kvadrata perimetrs: ", p)




nauda = int(input("Man ir: "))
abolu_cena = float(input("Abulu cena: "))
pirkums = int(input("Es nopirku: "))

kopa = abolu_cena*pirkums
atlikums = nauda - kopa

print("Atlikums: ",atlikums)