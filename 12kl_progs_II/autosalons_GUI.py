#===============================================
#Auto salona vadības sistēma
#===============================================
import itertools
import datetime
import fileinput
import PySimpleGUI as sg
sg.theme('DarkBlue')
#theme_name_list = sg.theme_list()
#print(theme_name_list)
 
class Produkts:
    Prod_kategorija = ""
    Prod_nosaukums = ""
    Prod_cena = ""

    
    id_iter = itertools.count()
    def __init__(self):
        self.Prod_id = next(self.id_iter)+1
        self.Prod_pieejams = True
        

    def __init__(self, _pakalpojums, _produkts, _cena):
        self.Prod_id = next(self.id_iter)+1
        self.Prod_kategorija = _pakalpojums
        self.Prod_nosaukums = _produkts
        self.Prod_cena = _cena
#        self.Prod_pieejams = True
        
    def __repr__(self):
        if self.Prod_kategorija: return self.prod_categorija
        elif self.Prod_nosaukums: return self.prod_nosaukums
        elif self.Prod_cena: return self.prod_cena
        return ''
    
    def Produkts_info(self):
        return [self.Prod_kategorija, self.Prod_nosaukums, self.Prod_cena]
    
    def Produkts_info_print():
        print("Produkta kategorija: " + str(self.Prod_kategorija))
        print("Produkta nosaukums: " + str(self.Prod_nosaukums))
        print("Pakalpojuma cena: " + str(self.Prod_cena))
        print("Pakalpojuma pieejamiba: " + str(self.Prod_pieejams) + "\n")    

class Klients:
    Klienta_vards=""
    Klienta_uzvards=""
    Klienta_PK=""
    Klienta_tel_numurs=0
    
    id_iter_nom = itertools.count()
    def __init__(self, _vards, _uzvards, _pk, _tel_numurs):
        self.Klienta_id = next(self.id_iter_nom)+1
        self.Klienta_vards = _vards
        self.Klienta_uzvards = _uzvards
        self.Klienta_PK = _pk
        self.Klienta_tel_numurs = _tel_numurs
        
    def Klients_info(self):
        return[self.Klienta_vards, self.Klienta_uzvards, self.Klienta_PK, self.Klienta_tel_numurs]
    
        
    def Klients_info_print(self):
        print("Klienta vards: " + self.Klienta_vards)
        print("Klienta uzvards: " + self.Klienta_uzvards)
        print("Klienta personas kods: " + self.Klienta_PK)
        print("Klienta telefona numurs: " + str(self.Klienta_tel_numurs) + "\n")
        
        

sadala1 = [[sg.Text('Bremžu pārbaude, eļļas un filtru maiņa,'"\n"'Riteņu konverģences un slīpuma regulēšana un tml.',font='Helvetica 14')],
           [sg.Text('Procedūras kategorija',size=(24,1)),sg.Input('',key='_pakalpojums')],
           [sg.Text('Remonts pēc avārijas, Pīlings, Pārbaude un tml.',font='Helvetica 16')],
           [sg.Text('Pakalpojuma nosaukums',size=(24,1)),sg.Input('',key='_produkts')],
           [sg.Text('Pakalpojuma cena',size=(24,1)),sg.Input('',key='_cena')],
           [sg.Button('Saglabat pakalpojuma datus')], 
           
           #def __init__(self, _vards, _uzvards, _pk, _tel_numurs):
           [sg.Text('Klienta vards', size=(22,1)),sg.Input('',key='_vards')],
           [sg.Text('Klienta uzvards', size=(22,1)),sg.Input('',key='_uzvards')],
           [sg.Text('Personas kods', size=(22,1)),sg.Input('',key='_pk')],
           [sg.Text('Telefons', size=(22,1)),sg.Input('(+371)  ',key='_tel_numurs')],
           [sg.Button('Saglabat klienta datus')], 

           #def __init__(self, sakDat, beigDat, idProdukts, idNomnieks, daudzums, cenaDiena, sodienasDat):
           [sg.Text('Sakuma datums', size=(22,1)),sg.Input('',key='sakDat')],
           [sg.Text('Sakuma laiks', size=(22,1)),sg.Input('',key='sakTime')],
           [sg.Text('Produkta id', size=(22,1)),sg.Input('',key='idProdukts')],
           [sg.Text('Klienta id', size=(22,1)),sg.Input('',key='idKlients')],
           [sg.Text('Pakalpijuma daudzums', size=(22,1)),sg.Input('',key='daudzums')],
           
           [sg.Text('Sodienas datums', size=(22,1)),sg.Input('',key='sodienasDat')],
           [sg.Button('Saglabat Auto salona pakalpojuma datus')]]

sadala2 = [[sg.Button('Pakalpojuma info, izvada uz ekrana')],
          [sg.Button('Klienta info, izvada uz ekrana')],
          
          [sg.Button('Cena par pakalpujumu, izvada uz ekrana')]]

sadala3 = [[sg.Button('Pakalpojums: veidot atskaiti teksta faila formata')],
          [sg.Button('Klients: veidot atskaiti teksta faila formata')]]


sadalu_grupa = [[sg.TabGroup
               ([[sg.Tab('Datu ievade', sadala1),
               sg.Tab('Datu izvade', sadala2),
               sg.Tab('Atskaites printesana', sadala3)]]),
               sg.Button('Aizvert',pad=(0,0,1),font='Helvetica 14')]]

           
window =sg.Window("Auto salons",sadalu_grupa)

file=open("Pakalpojuma_atskaite.txt", "w")
file=open("Klienta_atskaite.txt", "w")

while True: 
  event, values = window.read()
  if event == sg.WIN_CLOSED or event == 'Aizvert':
    break

#======================================= 1 sadala ===============
  elif event == 'Saglabat pakalpojuma datus':
    prod = Produkts(values['_pakalpojums'], values['_produkts'], values['_cena'])

  elif event == 'Saglabat klienta datus':
    klients = Klients(values['_vards'], values['_uzvards'], values['_pk'], values['_tel_numurs'])      
  elif event == 'Saglabat Auto salona pakalpojuma datus':
    prod = Pakalpojums(values['sakDat'],values['sakTime'],values['idProdukts'],values['idKlients'],values['daudzums'],values['sodienasDat'])

 
#======================================= 2 sadala ===============
  elif event == 'Pakalpojuma info, izvada uz ekrana':
    prod.Produkts_info_print()
  elif event == 'Klienta info, izvada uz ekrana':
    klients.Klients_info_print()
  
    


#======================================= 3 sadala ===============
  elif event == 'Pakalpojums: veidot atskaiti teksta faila formata':
    file=open("Pakalpojuma_atskaite.txt", "a")
    file.write(str(prod.Produkts_info()))
    file.write("\n")
    file.close()

  elif event == 'Klients: veidot atskaiti teksta faila formata':
    file=open("Klienta_atskaite.txt", "a")
    file.write(str(klients.Klients_info()))
    file.write("\n")
    file.close()

window.close() #aizver logu saskarnei
