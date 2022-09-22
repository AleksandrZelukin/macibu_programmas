#Programma pieprasa kvadrāta mālu a un izskaitļo perimetru 

print("Ievadi, lūdzu kvadrāta mālu:")

def perimetrs (a):
    return a*4

a=int(input())
b = perimetrs(a)

print("Kavdrāta perimetrs ir: ", b)

#Programma pieprasa Kārļa trīs atzīmes un izskaitļo vidējo aritmētisko

def atzimes (a1,a2,a3):
    return (a1+a2+a3)/3
print("Ievadi, lūdzu atzīmi 1. :")
x = int(input())
print("Ievadi, lūdzu atzīmi 2. :")
y = int(input())
print("Ievadi, lūdzu atzīmi 3. :")
z = int(input())

v=atzimes(x,y,z)

print("Vidēja atzīmi ir: ", v)

#Kārlis noperka M kg abolu maksājot C centus par kg. 
#Cik centus X ir jāsamaksa par pirkumu? 
#Cik atlikuma centus S viņš dabūs no L eiro?

def aboli(M=3,L=5,C=0.49):
    return M*C

M = int(input("Kārlis noperka abolus (kg)"))
L= int(input("Kārlim bija: (eiro)"))
C = float(input("Cena par kilo abolus (eiro): "))
X = M*C
S = L-X
y = aboli (M,L,C)
print("Kārlis samaksa ",y,"eiro")
print("Kārlim palīka ", S, "eiro")

#Annai ir a gadi, bet Marutai - m gadi. Kas no viņam ir vecāka? 

a = int(input("Annai ir :"))
m = int(input("Marutai ir :"))

def vecums(a,m):
    if a==m:
        return 'Anna un Maruta viena vecumā'
    elif a<m: return "Maruta ir vecāka"
    else: return "Anna ir vecāka"


print(vecums(a,m))


#Pļavā rotaļājas bērni un suņi. Zinot galvu un kāju kopējo skaitu (g un k), 
#atrast, cik bērnu un cik suņu ir pļavā (b un s). 
g = int(input("Galvas: "))
k = int(input("Kājas: "))   

g = int(input("Galvas: "))
k = int(input("Kājas: "))

#pirmais variants
x=k-(g*2) #"liekas" kajas
s=x/2 #suņu skaits

b=g-s #bernus skaits



