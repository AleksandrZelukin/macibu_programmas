# import PySimpleGUI as sg
from PySimpleGUI import Input,Text, Button, Window, WINDOW_CLOSED

layout = [[Text("Kā tevi sauc?")],
          [Input(size=(20,1),key='-INPUT-')],
          [Text(text='Sveiki! ',size=(40,1), key='-OUTPUT-')],

          [Button('Ok'), Button('Quit')]]

window = Window('Jautājums', layout)

while True:
    event, values = window.read()

    window['-OUTPUT-'].update( values['-INPUT-'])
 
    if event == WINDOW_CLOSED or event == 'Quit':
        break

window.close()