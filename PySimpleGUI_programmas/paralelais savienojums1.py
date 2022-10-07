import PySimpleGUI as sg

def kopa (r1, r2):
    r1 = float(input())
    r2 = float(input())
    r = round(1/(1/r1+1/r2),2)
    return (f'Kopejas pretestiba: {r_par}')

layout = [[sg.Text("Paralelais savienojums")],
          [sg.Text("R1")],[sg.Input(key="r1")],
          [sg.Text("R2"),sg.Input(size=(10,1))],
            [sg.Button('cik?', key='submit')],
            [sg.Text('', key='r', size=(20,2))],
          [sg.Button('Ok'), sg.Button('Quit')]]


window = sg.Window('Jautājums', layout)


while True:
    event, values = window.read()

    if event == 'submit':
        r = kopa(r1,r2)
        window['r'].update (r)
        print(r)
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

window.close()