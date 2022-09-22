#Visam uzdevumam izveidot funkcijas (def)
#1 Programma pieprasa kvadrāta mālu a un izskaitļo perimetru 

print("Ievadi, lūdzu kvadrāta mālu:")
a=int(input())

p = a*4

print("Kavdrāta perimetrs ir: ", p)

#2 Programma pieprasa Kārļa trīs atzīmes un izskaitļo vidējo aritmētisko

print("Ievadi, lūdzu atzīmi 1. :")
a1 = int(input())
print("Ievadi, lūdzu atzīmi 2. :")
a2 = int(input())
print("Ievadi, lūdzu atzīmi 3. :")
a3 = int(input())

v=(a1+a2+a3)/3

print("Vidēja atzīmi ir: ", v)

#3 Kārlis noperka M kg abolu maksājot C centus par kg. 
#Cik centus X ir jāsamaksa par pirkumu? 
#Cik atlikuma centus S viņš dabūs no L eiro?

M = int(input("Kārlis noperka abolus (kg)"))
L= int(input("Kārlim bija: (eiro)"))
C = float(input("Cena par kilo abolus (eiro): "))
X = M*C
S = L-X

print("Kārlis samaksa ",X,"eiro")
print("Kārlim palīka ", S, "eiro")

#4 Annai ir a gadi, bet Marutai - m gadi. Kas no viņam ir vecāka? 

a = int(input("Annai ir :"))
m = int(input("Marutai ir :"))

if a==m:
    print("Annai un Marutai lizdigs vecums")
else:
    if a>m :
        print("Anna ir vecāka")
    
    else:
        print("Maruta ir vecāka")
     





