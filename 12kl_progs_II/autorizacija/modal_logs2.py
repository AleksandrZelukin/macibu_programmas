import PySimpleGUI as sg


def main():
    layout = [[sg.Button("Open Window", key="open")]]
    window = sg.Window("Main Window", layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "open":
            if sg.Window("Other Window", [[sg.Text("Try Again?")], 
                                          [sg.Yes(), sg.No()]]).read(close=True)[0] == "Yes":
                print("User chose yes!")
            else:
                print("User chose no!")
        
    window.close()


if __name__ == "__main__":
    main()