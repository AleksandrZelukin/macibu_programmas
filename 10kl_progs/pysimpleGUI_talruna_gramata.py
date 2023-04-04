import PySimpleGUI as sg

izkartojums = [[sg.Text('Vārds')],
               [sg.InputText()],
               [sg.Text('Talruna numurs')],
               [sg.InputText('(+371)')],
               [sg.Button('Saglabāt', key='s'),sg.Button('Beigt', key='q')]]

logs = sg.Window('Virsrāksts', izkartojums)
phonebook={}
while True:
    event, values = logs.read()
    if event == sg.WINDOW_CLOSED or event == 'q':
      break
    if event == 's':
      phonebook[values[0]]=values[1]
      print(phonebook)