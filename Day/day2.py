Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print('包含中文的str')
包含中文的str
>>> ord('A')
65
>>> #s
>>> 

>>> 
>>> 
>>> 
>>> ord('陈旭升')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    ord('陈旭升')
TypeError: ord() expected a character, but string of length 3 found
>>> ord('陈')
38472
>>> chr('65')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    chr('65')
TypeError: an integer is required (got type str)
>>> chr(88)
'X'
>>> chr(78953)
'\U00013469'
>>> chr(45454)
'놎'
>>> '\u4e2d]u6587'
'中]u6587'
>>> '\u4e2d\u6587'
'中文'
>>> x = b'ABC'
>>> print(x)
b'ABC'
>>> name = '陈旭升'
>>> print('name')
name
>>> print(name)
陈旭升
>>> name = '陈旭升,2.28'
>>> print(name)
陈旭升,2.28
>>> one = 1
>>> two = 2
>>> three = one + two
>>> print(three)
3
>>> myname = goodboy
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    myname = goodboy
NameError: name 'goodboy' is not defined
>>> myname = 'goodboy'
>>> shi = 'shi'
>>> xixi = '陈旭升'
>>> haha = myname + shi + xixi
>>> print(haha)
goodboyshi陈旭升
>>> myname
'goodboy'
>>> two
2
>>> '1'+'2'
'12'
>>> 1+'2'
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    1+'2'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> maybe
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    maybe
NameError: name 'maybe' is not defined
>>> 'let\'s go'
"let's go"
>>> str = 'C:\now'
>>> str
'C:\now'
>>> print(str)
C:
ow
>>> str  = 'C:\\now'
>>> str
'C:\\now'
>>> print(str)
C:\now
>>> str = r'C:\now'
>>> str
'C:\\now'
>>> print(str)
C:\now
>>> 'ABC'.encode('ascii')
b'ABC'
>>> '中文'.encode('utf-8')
b'\xe4\xb8\xad\xe6\x96\x87'
>>> len('she is love me')
14
>>> 中文
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    中文
NameError: name '中文' is not defined
>>> zhongwen
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    zhongwen
NameError: name 'zhongwen' is not defined
>>> str
'C:\\now'
>>> 'hello,%/'%world'
SyntaxError: EOL while scanning string literal
>>> 'hello,%/'% world'
SyntaxError: EOL while scanning string literal
>>> 'hello,%'% world'
SyntaxError: EOL while scanning string literal
>>> 'hello,%''%' world'
SyntaxError: invalid syntax
>>> 'hello,%s' % 'world'
'hello,world'
>>> 'hi,%%'
'hi,%%'
>>> 'hi,%s%'
'hi,%s%'
>>> 'hi,%s'%''
'hi,'

>>> print('%2d-%02d' % (3, 1))
 3-01
>>> 'hi,%s'
'hi,%s'
>>> 'hi,%s'%''
'hi,'
>>> 'hi,%s%'
'hi,%s%'
>>> 'hi,%s'%'s'
'hi,s'
>>> 'age:%s. Gender: %s (21, true)'
'age:%s. Gender: %s (21, true)'
>>> 'i want to write %%'
'i want to write %%'
>>> 'i want to write %%' %7
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    'i want to write %%' %7
TypeError: not all arguments converted during string formatting
>>> 'i want to write %d %%' %7
'i want to write 7 %'
>>> s1 = 72
>>> s2 = 85
>>> r = (s2-s1)/s1 * 100
>>> print('小明的成绩提升了:%.1f%%'.' % r)
      
SyntaxError: EOL while scanning string literal
>>> 
