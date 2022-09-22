# -*- coding: utf-8 -*-
import turtle as t #подключаем библиотеку для рисования
import random as rnd #подключаем библиотеку для случайных чисел

#Пишем полезные функции для рисования.
#функция для перевода пера в случайную точку.
def idem_v_sluchaynuyu_tochku(): 
    t.penup() #поднимаем перо над бумагой.
    t.setpos( rnd.randint(-200,200) , rnd.randint(-200,200)) #перемещаемся в случайную точку.
    t.pendown()  #опускаем перо на бумагу, чтобы снова рисовать.

#функция для рисования звезды.
def risuem_zvezdu(razmer, tsvet):
    t.color(tsvet) #задали цвет
    t.pendown() #опустили перо на бумагу.
    t.begin_fill() #начинаем заполнение цветом.
    for _ in range(5): #у звезды 5 сторон.
        t.left(144) #поворот на 144 градуса
        t.forward(razmer) #идём вперёд на размер звезды.
    t.end_fill() #заканчиваем заполнение цветом
    t.penup() #поднимаем перо над бумагой.

#функция для рисования галактики, состоящей из множества звёзд.
def risuem_galaktiku(skolko_zvezd):
    zvezdaColours = ["#2D959A","#7F2D9A","#9A5F2D","#95236A","#789523"] #на выбор берём один из 5 цветов для звезды.
    idem_v_sluchaynuyu_tochku() #переместимся в любое место на холсте, чтобы нарисовать галактику.
    #рисуем множество мелких звёздочек.
    for _ in range(skolko_zvezd):
        t.penup() #поднимаем перо.
        t.left( rnd.randint(-180,180)) #поворачиваем на случайный угол.
        t.forward(rnd.randint(5,20)) #идём на случайное короткое расстояние вперёд.
        t.pendown() #опускаем перо.
        risuem_zvezdu( 2, rnd.choice(zvezdaColours)) #рисуем мелкую звёздочку.

#функция для рисования созвездий.
def risuem_sozvezdie(skolko_zvezd):
    idem_v_sluchaynuyu_tochku()
    for _ in range(skolko_zvezd-1): #рисуем все звёзды созвездия кроме последней.
        risuem_zvezdu(rnd.randint(7,15), "#FFFF33") #вызываем функцию для рисования звёзд.
        t.pendown() #опускаем перо.
        t.left(rnd.randint(-90,90)) #поворачиваем налево на случайный градус.
        t.forward(rnd.randint(30,70)) #идём вперёд.
    risuem_zvezdu(rnd.randint(7,15), "#FFFF33") #рисуем последнюю звезду.
	
#Функции готовы, теперь сами действия по рисованию звёздного неба!
#t.shape ("turtle") #на наконечнике пера будет черепашка - turtle.
t.hideturtle() #прячем черепашку.
t.speed(100) #устанавливаем скорость рисования. 100 - это очень быстро.
print('Установили скорость пера')
t.bgcolor("#32127A") #задаём цвет неба.
print('Установили цвет неба')
print('Начинаем рисовать звёзды')
for zvezda in range(10): #рисуем 10 звёзд.
	idem_v_sluchaynuyu_tochku() #каждая звезда в случайной точке.
	risuem_zvezdu( rnd.randint(5,25) , "#FFFF33") #используем заготовленную функцию.
	print('Звезда № '+str(zvezda+1))
print('Начинаем рисовать галактики')
for galaktika in range(3): #рисуем три галактики.
	risuem_galaktiku(20) #используем заготовленную функцию.
	print('Галактика № '+str(galaktika+1))
print('Начинаем рисовать созвездия')
for sozvezdie in range(2): #рисуем два созвездия. 
	print('Созвездие № '+str(sozvezdie+1))
	risuem_sozvezdie(rnd.randint(4,7))
print('Всё нарисовано!')
t.hideturtle() #прячем черепашку.
t.done() #готово!
