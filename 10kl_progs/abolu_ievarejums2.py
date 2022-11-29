'''
https://siic-lv.github.io/programmesana/vidusskola/p1/specifikacija/
Specifikacija:
Nepieciešama iespēja definēt recepti un tās sastāvdaļas
Nepieciešama iespēja definēt, cik maksā katra sastāvdaļa
Sistēmai jāaprēķina kopējās ievārījuma izmaksas, balstoties uz ievadīto ābolu apjomu

'''
def izmaksas_receptei(recepte, cena):
    summa = 0
    for sastavdala, daudzums in recepte:
        summa += daudzums * cena[sastavdala]
    return summa

def izmaksas_kopa(abolu_svars):
    recepte = {"cukurs": 0.6, "kanelis": 0.08, "aboli": 2.0, "udens": 0.2}
    cenas = {"cukurs": 0.75, "kanelis": 30.0, "aboli": 0.0, "udens": 0.0}
    izmaksas_kg = izmaksas_receptei(recepte, cenas) / recepte["aboli"]
    return abolu_svars * izmaksas_kg

abolu_svars = 1.5
print("Uz {} kg ābolu izmaksas būs {} EUR".format(abolu_svars, izmaksas_kopa(abolu_svars)))

aboli = 5
print("Uz {} kg ābolu izmaksas būs {} EUR".format(aboli, izmaksas_kopa(aboli)))