#Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.
>>> import keyword
>>> print("Python keywords:", keyword.kwlist)
Python keywords: ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> a=4
>>> b=5
>>> id(a)
1613289696
>>> a=10
>>> b="hello"
>>> c=(1,2)
>>> type (a)
<class 'int'>
>>> type (b)
<class 'str'>
>>> type(c)
<class 'tuple'>
>>> 3+2
5
>>> a=3
>>> b=2
>>> a+b
5
>>> a=3
>>> b=2
>>> c=a+b
>>> print(c)
5
>>> 
>>> //Представление числа в шестнадцатеричной системе
SyntaxError: invalid syntax
>>> #Представление числа в шестнадцатеричной системе
>>> m=124504
>>> hex(m)
'0x1e658'
>>> oct(m)
'0o363130'
>>> bin(m)
'0b11110011001011000'
>>> b="hello"
>>> hex(a)
'0x3'
>>> import math
>>> math.factorial(7)
5040
>>> math.pi
3.141592653589793
>>> math.e
2.718281828459045
>>> 
