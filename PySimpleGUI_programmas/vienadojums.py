import PySimpleGUI as sg
from math import pi


layout = [
    [sg.Text("Введите высоту между r1 и r2:")], [sg.Input(key="-IN-0")],
    [sg.Text("Введите r1:")], [sg.Input(key="-IN-1")],
    [sg.Text("Введите r2:")], [sg.Input(key="-IN-2")],
    [sg.Text("Результат в Литрах", size=(30, 1), key="-OUT-")],
    [sg.Button("OK"), sg.Button("Выход")],
    [sg.Button("Стереть все")],
]

window = sg.Window("Вычислятель объема", layout)

while True:
    event, values = window.read()
    if event == "OK":
        # если поля пустые - ничего не делаем
        if "" in [values["-IN-0"], values["-IN-1"], values["-IN-2"]]:
            continue
        h = float(values["-IN-0"])
        r1 = float(values["-IN-1"])
        r2 = float(values["-IN-2"])
        x = (1 / 3) * pi * h * (r1 ** 2 + r1 * r2 + r2 ** 2)
        window["-OUT-"].update(x)
    elif event == "Стереть все":
        window["-IN-0"].update("")
        window["-IN-1"].update("")
        window["-IN-2"].update("")
        window["-OUT-"].update("")
    if event == "Выход" or event == sg.WIN_CLOSED:
        break


window.close()