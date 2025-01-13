import PySimpleGUI as sg 
layout = [[sg.Text('Sveiciens!')],
        [sg.InputText(key='-usr-')],
        [sg.Text(" ", size =(15, 1), font=40)],
        [sg.Button('Ok'),sg.Cancel()]]



window = sg.Window("Testa logs", layout)

while True:
    event,values = window.read()
    if event == "Cancel" or event == sg.WIN_CLOSED:
        break
    else:
        if event == "Ok":
            window.close()
            sg.popup("Welcome!")