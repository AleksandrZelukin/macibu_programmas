from PySimpleGUI import Text, InputText,Button,Window,WINDOW_CLOSED

izkartojums = [[Text('Vārds')],
               [InputText()],
               [Text('Talruna numurs')],
               [InputText('(+371)')],
               [Button('Saglabāt', key='s'),Button('Beigt', key='q')]]

logs = Window('Virsrāksts', izkartojums)
phonebook={}
while True:
    event, values = logs.read()
    if event == WINDOW_CLOSED or event == 'q':
      break
    if event == 's':
      phonebook[values[0]]=values[1]
      print(phonebook)