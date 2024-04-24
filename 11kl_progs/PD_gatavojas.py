#Definējiet funkciju "aprēķināt_vidējo", kas saņem trīs skaitļus 
# kā argumentus (atsevišķi) un atgriež to vidējo vērtību.

def aprēķināt_vidējo(sk1, sk2,sk3):
    return sk1+sk2+sk3/3

print(aprēķināt_vidējo(3,5,8))

#Definējiet funkciju "izvadit_virkni", kas saņem vienu argumentu - 
# virkni, un izvada šo virkni atpakaļ uz ekrānu.

def izvadit_virkni(virkni):
    return virkni

x = input()
print(izvadit_virkni(x))

#Uzrakstiet funkciju "uzskaite", kas ievada skaitli no 1 līdz 10 
# un izvada atbilstošo vārdu (piemēram, "vien", "divi", "trīs", utt.).

def uzskaite(skaitlis):
    skaitlu_vardnica = {1: "vien", 2: "divi", 3: "trīs", 4: "četri", 5: "pieci", 6: "seši", 7: "septiņi", 8: "astoņi", 9: "deviņi", 10: "desmit"}
    return skaitlu_vardnica.get(skaitlis, "Nederīgs skaitlis")

print(uzskaite(3))

#Uzrakstiet programmu, kas pārbauda, vai ievadītais gads ir garais gads 
# (ar 366 dienām) vai parasts gads (ar 365 dienām).

gads = int(input("Ievadiet gadu: "))
if (gads % 4 == 0 and gads % 100 != 0) or (gads % 400 == 0):
    print("Gads ir garais gads.")
else:
    print("Gads ir parasts gads.")

#Uzrakstiet programmu, kas prasa lietotājam ievadīt vārdu 
# un pēc tam izvada šo vārdu atpakaļ apgrieztā formā.

vards = input("Ievadiet vārdu: ")
apgriezts_vards = vards[::-1]
print("Apgrieztā formā:", apgriezts_vards)

#Uzrakstiet funkciju "aprēķināt_faktoriālu", 
# kas saņem vienu skaitli kā argumentu un atgriež tā faktoriālu.
def aprēķināt_faktoriālu(skaitlis):
    faktoriāls = 1
    for i in range(1, skaitlis + 1):
        faktoriāls *= i
    return faktoriāls

print(aprēķināt_faktoriālu(5))

#Uzrakstiet funkciju "parbaudīt_pāra_skaitli", kas saņem vienu skaitli kā argumentu un pārbauda, 
# vai tas ir pāra skaitlis vai nē. 
# Ja skaitlis ir pāra, funkcija atgriež True, ja nē - False.
def parbaudīt_pāra_skaitli(skaitlis):
    if skaitlis % 2 == 0:
        return True
    else:
        return False

print(parbaudīt_pāra_skaitli(6))

#Uzrakstiet programmu, kas izvada pirmos 10 veselos skaitļus sākot ar 1 un beidzot ar 10.
for skaitlis in range(1, 11):
    print(skaitlis, end=", ")
#Uzrakstiet funkciju "aprēķināt_kvadrātu", kas saņem vienu skaitli 
# kā argumentu un atgriež šī skaitļa kvadrātu.

def aprēķināt_kvadrātu(skaitlis):
    return skaitlis ** 2

print(aprēķināt_kvadrātu(5))




