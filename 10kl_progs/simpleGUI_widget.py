import PySimpleGUI as sg


layout = [[sg.Text('Sveiki, ka tev sauc?',size=(40))],
          [sg.InputText()],
          [sg.Text('',key='radit', size=(40))],
          [sg.Text('',key='sk', size=(40))],
          [sg.Button("Saglabāt datus", key='glab'),
           sg.Button("Skātit dati", key='skat'),
           sg.Button("Beigt", key='q')]]
  
logs = sg.Window('Mana pirma programma', layout)

while True:
    event, values = logs.read()
    if event == sg.WINDOW_CLOSED or event == 'q':
      break
    if event == 'skat':
      #  print(values[0])
       logs['sk'].update(values[0])
    if event == 'glab':
       logs['radit'].update('dati saglabāti')