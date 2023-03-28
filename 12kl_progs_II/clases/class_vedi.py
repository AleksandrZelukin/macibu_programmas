# Abstrakcija
class Viesis:
    def __init__(self,vards,parole):
        self.vards = vards
        self.parole = parole
    def drukaVardu(self):
        print('viesis '+f'{self.vards}'+ ' izveidots')
    def drukaParole(self):
        print('parole '+f'{self.parole}'+ ' izveidota')

# inkapsulacija
# vards = "Valdis" 
# parole = "123"
vards = input()
parole = input()

viesis1 = Viesis(vards,parole)

viesis1.drukaVardu()
viesis1.drukaParole()

# Manošana
class Darbinieki(Viesis):
    def drukaVardu(self):
        print('Darbinieks '+f'{self.vards}'+ ' izveidots')



vards = "Daina "
parole = "AAAA"
darbinieks1 = Darbinieki(vards,parole)
darbinieks1.drukaVardu()
darbinieks1.drukaParole()

# Polimorfisms
visi = [viesis1, darbinieks1]

for x in visi:
    x.drukaVardu()
    x.drukaParole()