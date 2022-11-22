import PySimpleGUI as sg

data = ['One', 'Two', 'Three', 'Four']
layout = [
    [sg.Combo(data, size=20, enable_events=True, key='COMBO')],
    [sg.Push(), sg.Button('Check')],
]
window = sg.Window('Title', layout)

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event in ('COMBO', 'Check'):
        index = window['COMBO'].widget.current()
        print(index)

window.close()