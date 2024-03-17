#from os import write
import PySimpleGUI as sg

layout = [[sg.Text('Vārds', size=(10, 1)), sg.InputText(key="-V-")],
    [sg.Text('Uzvārds', size=(10, 1)), sg.InputText(key="-U-")],     
    [sg.Button("Saglabat", key="glabt"),sg.Button("Beigt", key='q')],
    [sg.Text("",text_color='red',key="-R-")]]

window = sg.Window('Datu registracijas logs', layout)

while True:
  event, values = window.Read()
  if event == "q":
    break
  if event == "glabt":
    f = open("dati.txt","a")
    f.writelines(values["-V-"]+" ")
    f.writelines(values["-U-"]+"\n")
    f.close()
    window["-V-"].Update('')
    window["-U-"].Update('')
    window["-R-"].Update("Dati sglabati!")
  
  #print(event, values[0])
