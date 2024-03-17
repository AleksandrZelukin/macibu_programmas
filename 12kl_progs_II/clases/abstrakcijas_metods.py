from abc import ABC, abstractmethod  
class Gramata(ABC):  
  def gramatas_dati(self):  
    pass 
 
class Hobits(Gramata):  
  def gramatas_dati(self):  
    print("Hobits: Negaidīts ceļojums, Džons Ronalds Rūels Tolkīns")  
class HarijsPoters(Gramata):  
  def gramatas_dati(self):  
    print("Harijs Poters un Filozofu akmens, Džoanna Ketlīna Roulinga")  
class DaVinciKods(Gramata):  
  def gramatas_dati(self):  
    print("Da Vinči kods, Dens Brauns")  
 
gramata1 = Hobits()  
gramata1.gramatas_dati()  
gramata2 = HarijsPoters()  
gramata2.gramatas_dati()  
gramata3 = DaVinciKods()  
gramata3.gramatas_dati()  
 