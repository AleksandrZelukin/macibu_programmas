import PySimpleGUI as sg

izkartojums = [[sg.Text('Kads teksts')],
               [sg.Text('Kads cits teksts')],
               [sg.Button('Beigt', key='q')]]

logs = sg.Window('Virsrāksts', izkartojums)
while True:
    event = logs.read()
    if event == sg.WIN_CLOSED or event == 'q':
      break
