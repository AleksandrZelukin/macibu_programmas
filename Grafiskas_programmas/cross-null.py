#   https://all-python.ru/primery/krestiki-noliki.html

#game_run – в эту переменную будем записывать False при завершении игры, чтобы запретить делать ходы когда уже выявлен победитель.
#field – это будет двумерный список, в котором будут храниться кнопки игрового поля. 
#Ходом будет изменение надписи на кнопке на символ «X» или «O».
#cross_count в этой переменной мы будем отслеживать количество крестиков на поле. 
#Чтобы по выставлению пятого крестика, в случае если никто не выиграл фиксировать ничью.


from tkinter import *
import random
root = Tk()
root.title('Criss-cross')
game_run = True  
field = []
cross_count = 0


#Функция new_game будет вызываться при нажатии кнопки начала новой игры. 
#На поле убираются все крестики и нолики. Цвет кнопок делаем бледно-лиловым. 
#Устанавливаем глобальные переменные game_run и cross_count в начальные значения. 
#Это глобальные переменные к которым пытаемся обратиться из функции. 
#Поэтому перед попыткой изменить их значение, в Python надо использовать ключевое слово global.


def new_game():
    for row in range(3):
        for col in range(3):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'lavender'
    global game_run
    game_run = True
    global cross_count
    cross_count = 0

#Функция click будет вызываться после нажатия на поле, то есть при попытки поставить крестик. 
#Если игра еще не завершена, то крестик ставится. 
#После этого увеличиваем счетчик количества выставленных крестиков.
#Потом проверяем с помощью функции check_win, не победили ли мы этим ходом. 
#Если еще не выявлен победитель и есть еще ходы, 
#то выполняет ход компьютер функцией computer_move, и также после хода идет проверка выигрыша.

    
def click(row, col):
    if game_run and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        global cross_count
        cross_count += 1
        check_win('X')
        if game_run and cross_count < 5:
            computer_move()
            check_win('O')
            
#Функция check_win осуществляет проверку выигрыша. 
#Она перебирает все возможные комбинации полей, образующих линию и вызывает с ними функцию check_line. 
#Переменная smb – это символ «X» или «O», то есть крестики или нолики. 
#Если задан «O», то проверяется: не победил ли компьютер.
#Если зафиксирован выигрыш, то меняем цвет фона кнопок, составляющих линию на розовый. 
#А также записываем в game_run значение False.            
            
def check_win(smb):
    for n in range(3):
        check_line(field[n][0], field[n][1], field[n][2], smb)
        check_line(field[0][n], field[1][n], field[2][n], smb)
    check_line(field[0][0], field[1][1], field[2][2], smb)
    check_line(field[2][0], field[1][1], field[0][2], smb)

def check_line(a1,a2,a3,smb):
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
        a1['background'] = a2['background'] = a3['background'] = 'pink'
        global game_run
        game_run = False

#Ход компьютера рассчитывается в функции computer_move. Алгоритм его действий следующий:
#Проверка возможности победы. 
#Если компьютеру представился шанс победы – он не должен его упустить. 
#Сразу же делает победу.
#Проверка возможной победы противника за один ход. 
#Если игрок выставил два крестика в ряд, компьютер пытается разрушить планы игрока.
#Случайный ход. Так как победить нет возможности и нет угрозы проигрыша, 
#то выбирается случайное свободное поле. В бесконечном цикле wile перебираются случайные числа, 
#пока они не выпадут на не занятое поле.

        
def can_win(a1,a2,a3,smb):
    res = False
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == ' ':
        a3['text'] = 'O'
        res = True
    if a1['text'] == smb and a2['text'] == ' ' and a3['text'] == smb:
        a2['text'] = 'O'
        res = True
    if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb:
        a1['text'] = 'O'
        res = True
    return res

def computer_move():
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'O'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'O'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'O'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'O'):
        return
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'X'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'X'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'X'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'X'):
        return
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'O'
            break
    
#Все элементы графического интерфейса будем размещать с помощью упаковщика grid. 
#В цикле добавим кнопки игрового поля. Они будут храниться в двумерном список. 
#В языке программирования Python добавляют элементы в список с помощью метода append.
#Свойство colorspan у кнопки начала игры выставляем в 3, чтобы он занимал всю ширину таблицы    
    
        
for row in range(3):
    line = []
    for col in range(3):
        button = Button(root, text=' ', width=4, height=2, 
                        font=('Verdana', 20, 'bold'),
                        background='lavender',
                        command=lambda row=row, col=col: click(row,col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)
new_button = Button(root, text='new game', command=new_game)
new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')
root.mainloop()