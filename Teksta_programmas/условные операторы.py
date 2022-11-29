Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Условный оператор ветвления if
>>> if1:
	
SyntaxError: invalid syntax
>>> if 1:
	print("hello 1")

hello 1
>>> a=3
>>> if a==3
SyntaxError: invalid syntax
>>> a=3
>>> if a==3:
	print("hello2")

	
hello2
>>> lst=[1,2,3]
>>> if lst:
	print("hello 4")

	
hello 4
>>> #Конструкция if – else
>>> a=3
>>> if a>2:
	print("h")
else:
	print("l")

	
h
>>> a=17
>>> b= True if a>10 else False
>>> print(b)
True
>>> #Конструкция if – elif – else
>>> a = int(input("введите число:"))
if a < 0:
   print("Neg")
elif a == 0:
   print("Zero")
else:
   print("Pos")
   
SyntaxError: multiple statements found while compiling a single statement
>>> #Оператор цикла while
>>> a=0
>>> while a<7:
	print("A")
	a +=1

	
A
A
A
A
A
A
A
>>> #Операторы break и continue
>>> a=0
>>> while a>=0:
	if a==7:
	break
SyntaxError: expected an indented block
>>> a=0
>>> whole a>=0:
	
SyntaxError: invalid syntax
>>> a=0
>>> while a>=0:
	if a==7:
		break
	a+=1
	print ("A")

	
A
A
A
A
A
A
A
>>> #Оператор break  предназначен для досрочного прерывания работы цикла while.
>>> #иначе он бы продолжался бесконечно
>>> a=-1
>>> while a<10:
	a+=1
	if a>=7:
		continue
	print("A")

	
A
A
A
A
A
A
A
>>> #Оператор continue  запускает цикл заново, при этом код, расположенный после данного оператора, не выполняется.
>>> #При запуске данного кода символ “А” будет напечатан 7 раз, несмотря на то, что всего будет выполнено 11 проходов цикла.
>>> 
>>> #Оператор цикла for
>>> for i in range(5):
	print("Hello")

	
Hello
Hello
Hello
Hello
Hello
>>> 
