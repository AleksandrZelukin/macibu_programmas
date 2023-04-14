import PySimpleGUI as sg  # 28.nov 06:15
import csv


# ====================================================   Pakalpojums
class Pakalpojums:
    def __init__(self, uzvards, cena, datums, laiks):
        self.uzvards = uzvards
        self.cena = cena
        self.datums = datums
        self.laiks = laiks


# ====================================================    Izejvielas
class Izejvielas:
    def __init__(self, uzvards, derigums, derigums_atvertam, laiks):
        self.uzvards = uzvards
        self.derigums = derigums
        self.derigums_atvertam = derigums_atvertam
        self.laiks = laiks


# ====================================================    Persona
class Persona:
    def __init__(self, kods, numurs, vards, uzvards, datums, galvene, key_li, datne):
        self.datne = datne
        self.key_li = key_li
        self.vards = vards
        self.uzvards = uzvards
        self.mob_nr = numurs
        self.datums = datums
        self.galvene = galvene

    def saglaba(self, dati):  #====================== saglaba(self,dati)
        self.dati = dati  # delimiter="'",
        with open(self.datne, 'w', newline='') as csv_datne:
            ierakstit = csv.writer(csv_datne, delimiter=',')
            for rinda in self.dati:
                ierakstit.writerow(rinda)

    def nolasa(self):  #==================================   nolasa(self)
        try:
            with open(self.datne, 'r', newline='') as csv_datne:
                dati = csv.reader(csv_datne, delimiter=',', quoting=csv.QUOTE_NONE)
                dati = list(dati)
            return dati
        except:
            print('Lūdzu datni,\"', self.datne, '\" ievietojiet')
            exit()
    def kodu(self):
        dat = self.nolasa()
        kods = []
        for rinda in dat:
            kods.append(rinda[0])
        return (kods)

    def layout_pers(self, kods,  key_li):  # ================   izkaartojums  #format = '%Y-%m-%d'
        izkarto_pers = [[sg.Text('Personas mob:'), sg.Listbox(kods, enable_events=True, key='-NRP'),
                         sg.Input(key='P-NRP-', enable_events=True, size=(20, 1))],
                        [sg.Text('        Vards:'), sg.Input(key='P-VARDS-', enable_events=True, size=(20, 1))],
                        [sg.Text('      Uzvards:'), sg.Input(key='P-UZVARDS-', enable_events=True, size=(20, 1))],
                        [sg.Button('Ievadīt klientu'), sg.Exit('Atcelt')]]
        return izkarto_pers

class Darbinieks(Persona):
    def layout_pers(self, kods,key_li):
        izkarto_pers = [[sg.Text('Darbinieka mob:'), sg.Listbox(kods, enable_events=True, key='-NRD'),
                         sg.Input(key='D-NR-', enable_events=True, size=(20, 1))],
                        [sg.Text('        Vards:'), sg.Input(key='D-VARDS-', enable_events=True, size=(20, 1))],
                        [sg.Text('      Uzvards:'), sg.Input(key='D-UZVARDS-', enable_events=True, size=(20, 1))],
                        [sg.CalendarButton('Datumi',target='D-DATUMS-', format='%Y-%m-%d'),
                         sg.Input(key='D-DATUMS-', enable_events=True, size=(70, 1)), ],
                        [sg.Button('Ievadīt dienas'), sg.Exit('Atcelt')]]
        return list(izkarto_pers)


class Klients(Persona):
    def layout_pers(self, kods, key_li):
        izkarto_pers = [[sg.Text('Klienta mob:'), sg.Listbox(kods, enable_events=True, key='-NRK'),
                         sg.Input(key='K-NR-', enable_events=True, size=(20, 1))],
                        [sg.Text('        Vards:'), sg.Input(key='K-VARDS-', enable_events=True, size=(20, 1))],
                        [sg.Text('      Uzvards:'), sg.Input(key='K-UZVARDS-', enable_events=True, size=(20, 1))],
                        [sg.CalendarButton('Apmeklēšanas datums',target='K-DATUMS-', format='%Y-%m-%d'),
                         sg.Input(key='K-DATUMS-', enable_events=True, size=(20, 1))],
                        [sg.Button('Ievadīt klientu'), sg.Exit('Atcelt')]]
        return list(izkarto_pers)


# ==================================================== main
key_ievad = ('-NR-', '-VARDS-', '-UZVARDS-', '-DATUMS-')
key_li = ('-NRD', '-NRK', '-NRP')
galvene = ['numurs', 'vards', 'uzvards', 'datums']
# ====================================================   dati saskarnei
darbinieks = Darbinieks('', '', '', '', '', galvene,  key_li, 'darbinieki.csv')
darbinieki = darbinieks.nolasa()
darbinieku_kod = darbinieks.kodu()

klients = Klients('', '', '', '', '', galvene, key_li, 'klienti.csv')
klienti = klients.nolasa()
klientu_kod = klients.kodu()

preces = [['krēms', 'pieniņš', 'špātulas']]
precu_kodi = [['P001', 'P002', 'P003']]
# ====================================================   izkaartojums
layout_preces = [[sg.Text('Preces:'), sg.Listbox(precu_kodi, enable_events=True, key='-NRP'),
                  sg.Input(key='P-NR-', size=(20, 1))],
                 [sg.Input(key='P-DATUMS-', size=(20, 1)), sg.CalendarButton('Termiņš', target='P-DATUMS-',
                                                                            default_date_m_d_y=(1, None, 2022))],
                 [sg.Button('Ievadīt preci'), sg.Exit('Atcelt')]]

# ====================================================     tabulaacijas

tab_group = sg.TabGroup([[
    sg.Tab("Darbinieki", darbinieks.layout_pers(darbinieku_kod, key_li), key='-TABD-'),
    sg.Tab("Klienti", klients.layout_pers(klientu_kod, key_li), key='-TABK-'),
    sg.Tab("Preces", layout_preces, key='-TABP-')
]])
col = [[tab_group]]
layout = [[sg.Column(col)]]
window = sg.Window('Skaistumkopšanas kabinets', layout)

# ====================================================    Notikumi:
event = ''
key_ievadi= ('D-NR-', 'D-VARDS-', 'D-UZVARDS-', 'D-DATUMS-','K-NR-', 'K-VARDS-', 'K-UZVARDS-', 'K-DATUMS-','P-NR-', 'P-DATUMS-')
vardnic_dati = {
    '-NRD': darbinieki,
    '-NRK': klienti,
    '-NRP': preces
}
vardnic_kodi = {
    '-NRD': darbinieku_kod,
    '-NRK': klientu_kod,
    '-NRP': precu_kodi
}
vardnic_key_ievad = {
    '-NRD': ('D-NR-', 'D-VARDS-', 'D-UZVARDS-', 'D-DATUMS-'),
    '-NRK': ('K-NR-', 'K-VARDS-', 'K-UZVARDS-', 'K-DATUMS-'),
    '-NRP': ('P-NR-', 'P-DATUMS-')
}
while event != sg.WIN_CLOSED and event != 'Atcelt':
    event, values = window.read()

    if event in key_li:  # meklee mob nr vai kodu
        dati = vardnic_dati[event]
        kodi = vardnic_kodi[event]
        key_ievad = vardnic_key_ievad[event]
        jauns = []
        text_event = event # viens no  ('-NRD', '-NRK', '-NRP')
        nr = kodi.index(values[event][0]) # atrod rindu ar izveleto numuru
        i=0
        for text_event in key_ievad: # klientam ('K-NR-', 'K-VARDS-', 'K-UZVARDS-', 'K-DATUMS-')
            values[text_event] = dati[nr][i] #nr rindaa kolonas i
            jauns.append(values[text_event])
            window[text_event].update(values[text_event]) # atjauno, lai redzetu teksta lauka
            i = i + 1

        if event == '-NRD':  # darbin mob.nr
            darbinieki=dati # darbinieku dati
        elif event == '-NRK':  # klientu mob.nr
            klienti=dati # klientu dati
        else:
            preces=dati
    elif event in key_ievadi: # kad ievadiits teksta laukaa
        dati = vardnic_dati['-NR'+event[0]] #'-NRD', '-NRK', '-NRP')
        kodi = vardnic_kodi['-NR'+event[0]]
        key_ievad = vardnic_key_ievad['-NR'+event[0]]
        i = 0 #key_ievad=('D-NR-', 'D-VARDS-', 'D-UZVARDS-', 'D-DATUMS-')
        jauns = []
        for text_event in key_ievad:
            jauns.append(values[text_event])
            window[text_event].update(values[text_event])  # atjauno, lai redzetu teksta lauka
            i = i + 1
    elif event == "Ievadīt klientu":  # nospiesta poga "Ievadīt"
        if len(jauns) >= 4 and '' not in jauns:
            sg.popup(jauns, background_color='#007733')
            flag = False
            for r in dati:
                try:
                    nr = r.index(jauns[0])  ### meklee numuru sarakstaa
                    flag = True
                except:
                    pass
            if flag:
                for k in range(4):
                    dati[nr + 1][k] = jauns[k]
            else:
                dati.append(jauns)
            klients.saglaba(dati)
        else:
            sg.popup('Kļūda', 'Aizpildīt visus laukus', background_color='#FF0000')
    elif event == 'Ievadīt dienas':  # nospiesta poga "Ievadīt"
        if len(jauns) >= 4 and '' not in jauns:
            sg.popup(jauns, background_color='#007733')
            flag = False
            for r in dati:
                try:
                    nr = r.index(jauns[0])  ### meklee numuru sarakstaa
                    flag = True
                except:
                    pass
            if flag:
                for k in range(4):
                    dati[nr + 1][k] = jauns[k]
            else:
                dati.append(jauns)
            darbinieks.saglaba(dati)
        else:
            sg.popup('Kļūda', 'Aizpildīt visus laukus', background_color='#FF0000')
window.Close()