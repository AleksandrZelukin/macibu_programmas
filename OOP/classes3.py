from re import A

a = ["Anna", 16, "11a"]
b= ["Janis", 17, "11b"]
c = ["Olga",18, "12a"]

print(a,'\n',b,'\n',c)


class Skolnieki:
    def __init__(self,vards,vecums,klase):
        self.vards = vards
        self.vecums = vecums
        self.klase = klase

    def drukat(self):
        print(self.vards,self.vecums,self.klase) 

a = Skolnieki('Anna',16,'11a')
b = Skolnieki('Janis',17,'11b')
c = Skolnieki('Olga',18,'12a')

a.drukat()
b.drukat()
c.drukat()