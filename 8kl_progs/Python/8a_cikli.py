while True:
    a = int(input('Skaitlis >> '))
    if a == 0:
        print("Programma beidz darbu!")
        break
    if a % 2 == 0:
        print('Skaitlis a ir paraskaitlis ')
    else:
        print('Skaitlis a ir NEparaskaitlis ')

a = 0
for i in range(1,10):
    print(a+i)
    i+=1