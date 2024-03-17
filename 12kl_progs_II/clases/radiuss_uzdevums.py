'''
1. uzdevums

Izveidot klasi "Rinkis", ar atribūtu "radiuss". 
Konstruktorā inicializēt parametru sākumvērtību. 
Ja metodē nepadod argumentus, tas sākumvērtības pēc noklusējuma uzstāda uz 1.

Jārealizē sekojošas metodes:  

1. Konstruktors #konstruktors ar parametru radiuss
2. iestatit_radiusu(radiuss) #uzstāda jaunu rādiusu, 
    ja rādiuss ir nulle vai negatīvs, tad uzstāda noklusējuma rādiusu 1.
3. izvadit_radiusu()  #izvada rādiusu
4. diametrs() # aprēķina diametru un izdrukā to

'''

class Rinkis:   #Izveidot klasi "Rinkis"
    
    def XXXXXXXX(self, radiuss):  #konstruktors ar parametru radiuss
        self.radiuss = radiuss   #konstruktorā inicializēt parametru sākumvērtību.

    def XXXXXXXXX(self, radiuss):
        if(radiuss <0 or radiuss == 0):  #ja rādiuss ir nulle vai negatīvs
            self.radiuss = 1  #tad uzstāda noklusējuma rādiusu 1
        else:                
            self.radiuss = radiuss # citādi rādiuss ir metodē dotais rādiuss

    def XXXXXXXXXX(self): #izvada rādiusu
        print(self.radiuss)

    def XXXXXXXXXX(self):   #aprēķina diametru
         print(2 * self.radiuss)

rad1=Rinkis(23)
rad1.diametrs()
rad1.izvadit_radiusu()

