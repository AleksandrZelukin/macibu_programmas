from cgitb import text
from curses import window
import PySimpleGUI as sg
def calc_bmi(h,w):
    try:
        h, w = float(h), float(w)
        bmi = round(w / h **2, 1)
        if bmi < 18.5:
            standard = "Extra vājš"
        elif 18.5 <= bmi <= 23.9:
            standard = "Normāls"
        elif 24.0 <= bmi <= 27.9:
            standard = "lieks svars"
        else:
            standard = "trekns"
    except (ValueError, ZeroDivisionError):
        return None
    else:
        return (f'BMI: {bmi}, {standard}')

layot = [[sg.Text("Augums"), sg.InputText (size=(25,1))],
        [sg.Text("Svars"), sg.InputText(size=(25,1))],
        [sg.Button("aprēķināt BMI", key='submit')],
        [sg.Text('', key='bmi', size=(20,2))],
        [sg.Button("Beigt", key='q')]]

window = sg.Window ("Calculator BMI", layot)

while True:
    event, values = window.read()
    if event == 'submit':
        bmi = calc_bmi(values[0], values[1])
        window['bmi'].update(bmi)
    if event == sg.WINDOW_CLOSED or event == 'q':
        break

    window.close()
