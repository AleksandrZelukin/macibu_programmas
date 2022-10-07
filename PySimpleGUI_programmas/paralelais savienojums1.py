import PySimpleGUI as sg

def kopa (r1, r2):
    r1, r2, = float(input(r1)), float(input(r2))
    r_par = round(1/(1/r1+1/r2),2)
    return (f'Kopejas pretestiba: {r_par}')

layout = [[sg.Text("Paralelais savienojums")],
          [sg.Text("R1"),sg.Input(key='R1')],
          [sg.Text("R2"),sg.Input(key='R2')],
          
          [sg.Text(size=(40,1), key='-OUTPUT-')],
            [sg.Button('cik?', key='submit')],
          [sg.Button('Ok'), sg.Button('Quit')]]


window = sg.Window('Jautājums', layout)


while True:
    event, values = window.read()

    if event == 'submit':
        r_par = kopa(values[0], values[1])
        window['r_par'].update (r_par)
        print(r_par)
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

window.close()