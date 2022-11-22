import PySimpleGUI as sg

choices = ['aaa', 'bbb', 'ccc']
layout = [  [sg.Combo(choices, k='-COMBO-')],
            [sg.Button('Go'), sg.Button('Exit')]  ]

window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Go':
        if values['-COMBO-'] in choices:
            idx = choices.index(values['-COMBO-'])
            print(f'Index = {idx}')
        else:
            print('Selection not in choices')

window.close()
