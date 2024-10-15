class Skolens:
    def dati(self, vards, vecums):
        self.vards = vards
        self.vecums = vecums
    def drukat(self):
        print(self.vards, self.vecums)

skolens = Skolens()
v = input("Skolēna vārds: ")
i = input("Sklēna vēcums: ")
skolens.dati(v,i)

skolens.drukat()
