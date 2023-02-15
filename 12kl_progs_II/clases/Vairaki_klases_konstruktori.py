'''

Saliec kodu pareizajā secībā, 
lai Python valodā tiktu izveidoti vairāki klases konstruktori, 
izmantojot atslēgvārdu "cls", 
nevis vienkārši ar noklusējuma vērtības piešķiršanu

Konstruktoru secība: 

0 kājas
2 kājas
4 kājas
100 kājas
Tad seko metode izdrukāt kāju skaitu.
Tad tiek veidotas objektu instances un pēctam izdrukāti rezultāti.

Rezultāts:

0
2
4
100

'''
#Всегда используйте self для первого аргумента для методов экземпляра.
#Всегда используйте cls для первого аргумента для методов класса.

class Dzivnieks:
    def __init__(self, kaju_skaits=0):
        self.kaju_skaits = kaju_skaits
    
    @classmethod
    def putns(cls): #cls подразумевает, что метод принадлежит классу
        return cls(2)

    @classmethod
    def majlops(cls):
        return cls(4)

    @classmethod
    def simtkajis(cls):
        return cls(100)

    def izdruka_kaju_skaitu(self): #self подразумевает, что этот метод связан с экземпляром класса
        print(self.kaju_skaits)


odze = Dzivnieks()
zoss = Dzivnieks.putns()
govs = Dzivnieks.majlops()
simtkajis = Dzivnieks.simtkajis()


odze.izdruka_kaju_skaitu()
zoss.izdruka_kaju_skaitu()
govs.izdruka_kaju_skaitu()
simtkajis.izdruka_kaju_skaitu()


