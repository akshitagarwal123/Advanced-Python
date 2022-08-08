Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 10/0
Traceback (most recent call last):   
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero  
>>> '10' + 9
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> D = {}
>>> D['rank']
Traceback (most recent call last):   
  File "<stdin>", line 1, in <module>
KeyError: 'rank'
>>> s = '19.45'
>>> int(s)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '19.45'
>>> open('xyz', 'r')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'xyz'
>>>