a = int(input())

if a % 3 == 0 and a % 6 == 0:
    print('Skaitlis ',a,'dalits uz 3 un 6')

else:
    print('Skaitlis ',a,'nedalits uz 3 un 6')

a = int(input('Mala a: '))
b = int(input('Mala b: '))

jautajums = input("Tas ir trijsturis vai taisnsturis?")
if jautajums == 'trijsturis':
    print('Trijstura laukums ir: ', a*b/2)
