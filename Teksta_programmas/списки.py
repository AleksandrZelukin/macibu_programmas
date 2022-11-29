Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Списки
>>> #Создание, изменение, удаление списков и работа с его элементами
>>> a=[]
>>> type(a)
<class 'list'>
>>> b=list()
>>> type(b)
<class 'list'>
>>> a=[1,2,23,,4,5,6,6]
SyntaxError: invalid syntax
>>> a=[1,2,3,4,5,6,7,8,9,0]
>>> type(a)
<class 'list'>
>>> #Добавление элемента в список осуществляется с помощью метода append()
>>> a=[]
>>> a.append(3)
>>> a.append("hello")
>>> print(a)
[3, 'hello']
>>> #Для удаления элемента из списка, в случае, если вы знаете его значение, используйте метод remove(x), при этом будет удалена первая ссылка на данный элемент.
>>> b=[2,3,5]
>>> print(b)
[2, 3, 5]
>>> b.remove(b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    b.remove(b)
ValueError: list.remove(x): x not in list
>>> b.remove(3)
>>> print(b)
[2, 5]
>>> 
