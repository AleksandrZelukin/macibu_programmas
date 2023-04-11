import PySimpleGUI as sg
import csv

#====================================================   Pakalpojums
class Pakalpojums:
    def __init__(self, uzvards, cena, datums, laiks):
        self.uzvards = uzvards
        self.cena = cena
        self.datums = datums
        self.laiks = laiks

#====================================================    Izejvielas
class Izejvielas:
    def __init__(self, uzvards, derigums, derigums_atvertam, laiks):
        self.uzvards = uzvards
        self.derigums = derigums
        self.derigums_atvertam = derigums_atvertam
        self.laiks = laiks

#====================================================    Persona
class Persona:
    def __init__(self, numurs, vards, uzvards, datums, galvene):
        self.vards = vards
        self.uzvards = uzvards
        self.mob_nr = numurs
        self.datums = datums
        self.galvene = galvene

    def saglaba(self, dati):  ######################## saglaba(self,dati)
        self.dati=dati  #delimiter="'",
        #print(self.dati)
        with open('kontakti.csv','w',newline='') as csv_datne:
            ierakstit = csv.writer(csv_datne, delimiter=',')
            for rinda in self.dati:
                ierakstit.writerow(rinda)

    def nolasa(self):  #############################   nolasa(self)
        try:
            with open('kontakti.csv','r', newline='') as csv_datne:
                klienti = csv.reader(csv_datne, delimiter=',', quoting=csv.QUOTE_NONE)
                dati = list(klienti)
            return dati
        except:
            print('Lūdzu datni \"kontakti.csv\" ievietojiet')
            exit()

#==================================================== main
galvene = ['numurs', 'vards', 'uzvards', 'datums']
pers = Persona('', '', '', '', galvene)
klienti = pers.nolasa()
#print('nolasiiijaaaa=',klienti)

#====================================================   dati saskarnei
mob = []

for rinda in klienti:
    mob.append(rinda[0])

preces = ['krēms', 'pieniņš', 'špātulas']

key_ievad = ('T-MOB-', 'T-VARDS-', 'T-UZVARDS-', 'T-DATUMS-')
key_li = ('-MOB-', '-VARDS-', '-UZVARDS-', '-DATUMS-')
layout_klienti = [[sg.Text('Klienta mob:'), sg.Listbox(mob,size=(20,1), enable_events=True, key='-MOB-'),
       sg.Input(key='T-MOB-', enable_events=True,size=(30, 1))],
      [sg.Text('        Vards:'), sg.Input(key='T-VARDS-',enable_events=True,  size=(20, 1))],
      [sg.Text('      Uzvards:'), sg.Input(key='T-UZVARDS-',enable_events=True,  size=(20, 1))],
      [sg.Input(key='T-DATUMS-', enable_events=True, size=(30, 1)), sg.CalendarButton('Apmeklēšanas datums',
        target='T-DATUMS-',  default_date_m_d_y=(1, None, 2022))],
      [sg.Button('Ievadīt klientu'), sg.Exit('Atcelt')]]
#====================================================   izkaartojums
layout_preces = [[sg.Text('Preces:'), sg.Listbox(preces, enable_events=True, key='listi'),
      sg.Input(key='-IN-', size=(20, 1))],
     [sg.Input(key='-DATUMS-', size=(20, 1)), sg.CalendarButton('Termiņš', target='-DATUMS-',
        default_date_m_d_y=(1, None, 2022))],
     [sg.Button('Ievadīt preci'), sg.Exit('Atcelt')]]

#====================================================     tabulaacijas
tab_group = sg.TabGroup([[
    sg.Tab("Klienti", layout_klienti, key="-TAB1-"),
    sg.Tab("Preces", layout_preces, key="-TAB2-")
]])
col = [[tab_group]]
layout = [[sg.Column(col)]]
window = sg.Window('Skaistumkopšanas kabinets', layout)
#====================================================    Notikumi:
event = "";jauns_klients = []
while event != sg.WIN_CLOSED and event != 'Atcelt':
    event, values = window.read()
    if event in key_li:  # atrod izveleto list notikumu
        if event == '-MOB-':
            nr = mob.index(values['-MOB-'][0])
            i=0
            for text_event in key_ievad:
                values[text_event] = klienti[nr][i] #no_list_tuple uz str
                jauns_klients.append(values[text_event])
                window[text_event].update(values[text_event]) # atjauno, lai redzetu teksta lauka
                i = i + 1
            #print('jaunie dati= ',jauns_klients)
        #text_event = 'T' + event  # parveido par atbiltosho teksta notikumu
    elif event in key_ievad:
        i = 0
        jauns_klients=[]
        for text_event in key_ievad:
            jauns_klients.append(values[text_event])
            #print('values[text_event] eventos = ',values[text_event])
            window[text_event].update(values[text_event])  # atjauno, lai redzetu teksta lauka
            i = i + 1
        #print(jauns_klients)
    elif event == "Ievadīt klientu":  # nospiesta poga "Ievadīt"
        #print(len(jauns_klients),jauns_klients )
        if len(jauns_klients)>=4 and '' not in jauns_klients:
            sg.popup(jauns_klients, background_color='#007733')
            #print("jaunieee klienti===",klienti[1],type(jauns_klients[0]))
            flag = False
            for r in klienti:
                try:
                    nr = r.index(jauns_klients[0])  ### meklee numuru sarakstaa
                    flag = True
                except:
                    pass
            if flag :
                for k in range(4):
                    klienti[nr+1][k] = jauns_klients[k]
            else:
                klienti.append(jauns_klients)
            pers.saglaba(klienti)
        else:
            sg.popup('Kļūda', 'Aizpildīt visus laukus', background_color='#FF0000')
window.Close()
