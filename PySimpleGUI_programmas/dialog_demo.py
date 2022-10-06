import PySimpleGUI as sg


layout = [[sg.Text("Kā tevi sauc?")],
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],

          [sg.Button('Ok'), sg.Button('Quit')]]


window = sg.Window('Jautājums', layout)


while True:
    event, values = window.read()

    window['-OUTPUT-'].update( values['-INPUT-'])
 
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

window.close()