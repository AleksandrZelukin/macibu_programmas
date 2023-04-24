from PySimpleGUI import Text, InputText,Button,Window,WINDOW_CLOSED
import csv

izkartojums = [[Text('Vārds')],
               [InputText()],
               [Text('Talruna numurs')],
               [InputText('(+371)')],
               [Button('Saglabāt', key='s'),Button('Beigt', key='q')]]

logs = Window('Virsrāksts', izkartojums)
phonebook=[]
while True:
    event, values = logs.read()
    if event == WINDOW_CLOSED or event == 'q':
      break
    if event == 's':
      # phonebook[values[0]]=values[1]
      # print(phonebook)
      # phonebook.append(values[0])
      # phonebook.append(values[1])
      with open('talruna_gramata.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow({values[0],values[1]})

