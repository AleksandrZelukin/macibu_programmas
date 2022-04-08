from tkinter import *
import random
win = Tk()
win.geometry('400x400')
win.title('akmens-papirs-šķēres')
win.config(bg ='#80dfff')
Label(win, text = 'akmens, papirs ,šķēres' ).pack()


choices = StringVar()
Label(win, text = 'akmens-papirs-šķēres!!! Lūdzu izvēlies!!' ).place(x = 20,y=70)
Entry(win, textvariable = choices ).place(x=90 , y = 130)

computer = random.randint(1,3)
if computer == 1:
    computer = 'akmens'
elif computer ==2:
    computer = 'papirs'
else:
    computer = 'šķēres'


Result = StringVar()
def play():
    ch = choices.get()
    if ch == computer:
        Result.set('Its a Tie')
    elif ch == 'papirs' and computer == 'akmens':
        Result.set('Dators izvēlas  akmens!!You Win!!')
    elif ch == 'papirs' and computer == 'šķēres':
        Result.set('Dators izvēlas  šķēres!!You Lose!!')
    elif ch == 'akmens' and computer == 'papirs':
        Result.set('Dators izvēlas  papirs!! You Lose!!')
    elif ch == 'akmens' and computer == 'šķēres':
        Result.set('Dators izvēlas  šķēres!!You Win!!')
    elif ch == 'šķēres' and computer == 'akmens':
        Result.set('Dators izvēlas  akmens!!You Lose!!')
    elif ch == 'šķēres' and computer == 'papirs':
        Result.set('Dators izvēlas  papirs!!You Win!!')
    else:
        Result.set('Nepareizi: Lūzdu izvēleties: akmens, papirs, šķēres')


def Reset():
    Result.set("") 
    choices.set("")

def Exit():
    win.destroy()

Entry(win, textvariable = Result,width = 50,).place(x=25, y = 250)
 
Button(win, text = 'PLAY'  ,padx =5, command = play).place(x=150,y=190)
 
Button(win, text = 'RESET' ,padx =5, command = Reset).place(x=70,y=310)
 
Button(win, text = 'EXIT'  ,padx =5, command = Exit).place(x=230,y=310)
 
 
win.mainloop()
