import PySimpleGUI as sg

# Define the window's contents
class logs:
    layout = [[sg.Text("Kartes numurs")],
          [sg.Input('1234567899', key='-INPUT-')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')],
          [sg.Button('Parbaudit')]]
# Create the window
    window = sg.Window('Jautājums', layout)

# Display and interact with the Window using an Event Loop
    while True:
        event, values = window.read()
    # See if user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break
    # Output a message to the window
    # window['-OUTPUT-'].update(values['-INPUT-'])
        print(values['-INPUT-'])

# Finish up by removing from the screen
    window.close()