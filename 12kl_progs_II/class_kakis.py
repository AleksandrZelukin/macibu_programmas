class Skola:
    def __init__(self, klase, vards):
        self.klase=klase
        self.vards=vards
    def drukat(self):
        print(self.vards,self.klase)


a1 = Skola("12a", "Vlada")
a2 = Skola("12a", "Olegs")
a3 = Skola("12b", "Kristīne")

a1.drukat()
a2.drukat()
a3.drukat()
