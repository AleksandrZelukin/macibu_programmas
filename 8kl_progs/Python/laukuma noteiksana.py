a = int(input('Mala a: '))
b = int(input('Mala b: '))

jaut = input('''
Trijsturis - 1
Taisnsturis - 2
''')
if jaut == '1':
    print('Trijstura laukums ir: ', a*b/2)
elif jaut == '2':
    print('Taismstura laukums ir: ', a*b)
else:
    print("nepareizi ievadidi dati")