Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> '{1} love {0}.{2}'.format('i','my','anything')
'my love i.anything'
>>> '{0} love {a}.{c}'.format('I',a='my',c='family')
'I love my.family'
>>> print('\ta')
	a
>>> print('\\')
\
>>> print(\)
	
SyntaxError: unexpected character after line continuation character
>>> print()

>>> print('\')
      
SyntaxError: EOL while scanning string literal
>>> 

>>> '%c' % 12
'\x0c'
>>> '%c' $ 97
SyntaxError: invalid syntax
>>> '%c' % 97
'a'
>>> '%c %c %c' % (97, 98, 99)
'a b c'
>>> % 'i love you'
SyntaxError: invalid syntax
>>> '%s' % 'i love you'
'i love you'
>>> '%d + %d = %d' % '41, 45, = 41 + 45'
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    '%d + %d = %d' % '41, 45, = 41 + 45'
TypeError: %d format: a number is required, not str
>>> '%d + %d = %d' % '41, 45 = 41 + 45'
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    '%d + %d = %d' % '41, 45 = 41 + 45'
TypeError: %d format: a number is required, not str
>>> '%d + %d = %d' % '41, 45, 41 + 45'
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    '%d + %d = %d' % '41, 45, 41 + 45'
TypeError: %d format: a number is required, not str
>>> '%d + %d = %d' % ('41, 45, 41 + 45')
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    '%d + %d = %d' % ('41, 45, 41 + 45')
TypeError: %d format: a number is required, not str
>>> '%d + %d = %d' % (41, 45, 41 + 45)
'41 + 45 = 86'
>>> '%o' % 16
'20'
>>> '%o' % 8
'10'
>>> '%x' % 16
'10'
>>> '%x' % a
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    '%x' % a
NameError: name 'a' is not defined
>>> '%x' % 'a'
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    '%x' % 'a'
TypeError: %x format: an integer is required, not str
>>> '%x' % ('a')
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    '%x' % ('a')
TypeError: %x format: an integer is required, not str
>>> '%x' % 1
'1'
>>> '%x' % 10
'a'
>>> '%x' % 16
'10'
>>> '%x' % 12
'c'
>>> '%X' % a0
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    '%X' % a0
NameError: name 'a0' is not defined
>>> '%X' % 150
'96'
>>> '%X' % 1
'1'
>>> '%X' % 32
'20'
>>> '%X' % 160
'A0'
>>> '%X' % 320
'140'
>>> '%X' % 1600
'640'
>>> '%f' % 16
'16.000000'
>>> '%5.4d' % 16
' 0016'
>>> '%+5.4d' % 16
'+0016'
>>> '#+5.4d' % 16
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    '#+5.4d' % 16
TypeError: not all arguments converted during string formatting
>>> '#5.4d' % 16
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    '#5.4d' % 16
TypeError: not all arguments converted during string formatting
>>> '%#o' % 13
'0o15'
>>> '%06d' % 5
'000005'
>>> '%-06d' % 5
'5     '
>>> '%+06d' % 5
'+00005'
>>> \a
SyntaxError: unexpected character after line continuation character
>>> '\a'
'\x07'
>>> a = list()
>>> a
[]
>>> b = 'i love you'
>>> b
'i love you'
>>> b = list(b)
>>> 
>>> b
['i', ' ', 'l', 'o', 'v', 'e', ' ', 'y', 'o', 'u']
>>> b =a
>>> b
[]
>>> c = (1, 1, 2, 3, 5, 8, 13, 21, 34)
>>> c
(1, 1, 2, 3, 5, 8, 13, 21, 34)
>>> c = list(c)
>>> c
[1, 1, 2, 3, 5, 8, 13, 21, 34]
>>> a = [1, 'a']
>>> a
[1, 'a']
>>> max(a)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    max(a)
TypeError: '>' not supported between instances of 'str' and 'int'
>>> a = [2.5,45454,125.5454]
>>> sum(a)
45582.0454
>>> sum(a, 1)
45583.0454
>>> a
[2.5, 45454, 125.5454]
>>> sorter(a)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    sorter(a)
NameError: name 'sorter' is not defined
>>> sorted(a)
[2.5, 125.5454, 45454]
>>> revered(a)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    revered(a)
NameError: name 'revered' is not defined
>>> reversed(a)
<list_reverseiterator object at 0x02EAAA50>
>>> list(reversed(a))
[125.5454, 45454, 2.5]
>>> list(enumerate(a))
[(0, 2.5), (1, 45454), (2, 125.5454)]
>>> a = [1, 2, 3, 4, 5, 6, 7]
>>> b = [2, 3, 4, 5]
>>> list(zip(a, b))
[(1, 2), (2, 3), (3, 4), (4, 5)]
>>> [(1, 2), (2, 3), (3, 4), (4, 5)]
[(1, 2), (2, 3), (3, 4), (4, 5)]
>>> a = '
SyntaxError: EOL while scanning string literal
>>> a = ['a', 'b']
>>> list(zip(a, b))
[('a', 2), ('b', 3)]
>>> def func():
	print('this is my function')

	
>>> def func():
	print('this is my function')
	print('首字母忘记大写了')
	print('关键字是'def'哦')
	
SyntaxError: invalid syntax
>>> def func():
	print('this is my function')
	print('首字母忘记大写了')
	print('关键字是def哦')

	
>>> def
SyntaxError: invalid syntax
>>> func()
this is my function
首字母忘记大写了
关键字是def哦
>>> tt()
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    tt()
NameError: name 'tt' is not defined
>>> def func(name):
	print(name + '我爱你!')

	
>>> func()
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    func()
TypeError: func() missing 1 required positional argument: 'name'
>>> func('尤靖茹')
尤靖茹我爱你!
>>> def add(num1, num2):
	result = num1 + num2
	print(result)

	
>>> add(1, 2)
3
>>> add(1, 2, 3)
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    add(1, 2, 3)
TypeError: add() takes 2 positional arguments but 3 were given
>>> add(8, 0)
8
>>> 
