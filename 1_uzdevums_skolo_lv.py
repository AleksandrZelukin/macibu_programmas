'''
Kā ar programmēšanas palīdzību risināt problēmas?
Sasniedzamais rezultāts: Izstrādāju vienkāršu programmatūru 
atbilstoši programmatūras prasību specifikācijai un uzdevumam.
1. uzdevums: Lasi, analizē, atpazīsti risinājumu!
Lasi un analizē doto problēmas aprakstu un specifikāciju! 
Atbildi uz jautājumiem!
● Vai specifikācijā ir minēts viss, kas nepieciešams, 
lai uzrakstītu programmu, kas to realizē? 
● Kāda papildu informācija nepieciešama?
● Kurš(-i) no dotajiem programmas piemēriem varētu 
būt šīs specifikācijas realizācija?
'''

#Uzrakstīt funkciju, kas aprēķina ābolu ievārījuma izmaksas.
def aprekins(a,c):
    s = a * c
    print ("Summa: ", + s)

#Uzrakstīt funkciju, kas aprēķina ābolu ievārījuma izmaksas, 
# ja dota cukura cena kilogramā un ābolu daudzums kilogramos.
def f(a, b, c, d):
    r = a*b / d
    print (r)
    return r

# Uzrakstīt funkciju, kas aprēķina ābolu ievārījuma izmaksas, 
# ja dota cukura cena kilogramā, cukura, ābolu un 
# garšvielu daudzums ievārījuma receptē, ābolu daudzums kilogramos.

def ievarijums(aboli_svars, cukurs_cena, cukurs_uz_kg):
    izmaksa_kg = cukurs_cena * cukurs_uz_kg
    izmaksas = izmaksa_kg * aboli_svars
    print (izmaksas)

def izmaksas_receptei (recepte, cena):
    #Funkcija aprēķina izmaksas dotai receptei 
    # summējot visu sastāvdaļu izmaksas
    
    summa = 0

    for sastavdala in recepte:
        daudzums = recepte[sastavdala]
        summa += daudzums * cena[sastavdala]
    return summa

    def izmaksas_kopa(abolu_svars, recepte, cenas):
        # Funkcija aprēķina izmaksas dotam daudzumam ābolu 
        # izmantojot dotu recepti un cenu sarakstu

        #Izmaksas uz vienu kilogramu ābolu
        Izmaksas_kg = izmaksas_receptei(recepte, cenas) / recepte["aboli"]

        #Izmaksas uz doto daudzumu ābolu
        ievarijuma_izmaksas = abolu_svars * izmaksas_kg

        print("Uz {} kg ābolu izmaksas būs {.2f} EUR".format(abolu_svars, ievarijuma_izmaksas))


        # Piemers lietošanai

        recepte1 = {"cukurs": 0.6, "kanelis": 0.008, "aboli": 2.0, "ūdens": 0.2}
        cenas1 = {"cukurs": 0.75, "kanelis": 30.8, "aboli": 0.0, "ūdens": 0.0}

        izmaksas_kopa(15.0, recepte1, cenas1)
