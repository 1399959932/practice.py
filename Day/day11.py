Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> dict1 = {}
>>> dict1.fromkeys((1, 2, 3))
{1: None, 2: None, 3: None}
>>> dict1.formkeys((1, 2, 3, 'Number'))
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    dict1.formkeys((1, 2, 3, 'Number'))
AttributeError: 'dict' object has no attribute 'formkeys'
>>> dict1.formkeys((1, 2, 3), 'Number')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    dict1.formkeys((1, 2, 3), 'Number')
AttributeError: 'dict' object has no attribute 'formkeys'
>>> dict1.fromkeys((1, 2, 3), 'Number')
{1: 'Number', 2: 'Number', 3: 'Number'}
>>> dict1.fromkeys((1, 2, 3), ('one', 'two', 'three'))
{1: ('one', 'two', 'three'), 2: ('one', 'two', 'three'), 3: ('one', 'two', 'three')}
>>> dict1 = dict1.fromkeys(range(32). 'k')
SyntaxError: invalid syntax
>>> dict1 = dict1.fromkeys(range(32). 'k'))
SyntaxError: invalid syntax
>>> dict1 = dict1.fromkeys(range(32), 'k')
>>> dict1
{0: 'k', 1: 'k', 2: 'k', 3: 'k', 4: 'k', 5: 'k', 6: 'k', 7: 'k', 8: 'k', 9: 'k', 10: 'k', 11: 'k', 12: 'k', 13: 'k', 14: 'k', 15: 'k', 16: 'k', 17: 'k', 18: 'k', 19: 'k', 20: 'k', 21: 'k', 22: 'k', 23: 'k', 24: 'k', 25: 'k', 26: 'k', 27: 'k', 28: 'k', 29: 'k', 30: 'k', 31: 'k'}
>>> for eachKey in dict1.keys():
	print(eachKey)

	
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
>>> for eachValue in dict1.Value():
	print(eachValue)

	
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    for eachValue in dict1.Value():
AttributeError: 'dict' object has no attribute 'Value'
>>> for eachValue in dict1.Values():
	
	print(eachValue)

	
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    for eachValue in dict1.Values():
AttributeError: 'dict' object has no attribute 'Values'
>>> for eachValue in dict1.values():
	
	print(eachValue)

	
k
k
k
k
k
k
k
k
k
k
k
k
k
k
k
k
k
k
k
k
k
k
k
k
k
k
k
k
k
k
k
k
>>> for eachItem in dict1.items():
	print(eachItem)

	
(0, 'k')
(1, 'k')
(2, 'k')
(3, 'k')
(4, 'k')
(5, 'k')
(6, 'k')
(7, 'k')
(8, 'k')
(9, 'k')
(10, 'k')
(11, 'k')
(12, 'k')
(13, 'k')
(14, 'k')
(15, 'k')
(16, 'k')
(17, 'k')
(18, 'k')
(19, 'k')
(20, 'k')
(21, 'k')
(22, 'k')
(23, 'k')
(24, 'k')
(25, 'k')
(26, 'k')
(27, 'k')
(28, 'k')
(29, 'k')
(30, 'k')
(31, 'k')
>>> print(dict1[31])
k
>>> print(dict1.get(32))
None
>>> print(dict1.get(32, '木有'))
木有
>>> print(dict1.get(31, '木有'))
k
>>> a = {1:'one', 2:'}
     
SyntaxError: EOL while scanning string literal
>>> a = {1:'one', 2:'two', 3:'three'}
>>> b = a
>>> c = b.copy()
>>> b
{1: 'one', 2: 'two', 3: 'three'}
>>> c
{1: 'one', 2: 'two', 3: 'three'}
>>> id(a)
51869856
>>> id(b)
51869856
>>> id(c)
51870336
>>> a.pop(2)
'two'
>>> a
{1: 'one', 3: 'three'}
>>> b
{1: 'one', 3: 'three'}
>>> b.pop()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    b.pop()
TypeError: pop expected at least 1 arguments, got 0
>>> b.popitem()
(3, 'three')
>>> b
{1: 'one'}
>>> c
{1: 'one', 2: 'two', 3: 'three'}
>>> a
{1: 'one'}
>>> c
{1: 'one', 2: 'two', 3: 'three'}
>>> b
{1: 'one'}
>>> c
{1: 'one', 2: 'two', 3: 'three'}
>>> c.setdefault('white')
>>> c
{1: 'one', 2: 'two', 3: 'three', 'white': None}
>>> b
{1: 'one'}
>>> b = {'小白':'狗'}
>>> c.update(b)
>>> c
{1: 'one', 2: 'two', 3: 'three', 'white': None, '小白': '狗'}
>>> num = {}
>>> type(num)
<class 'dict'>
>>> num1 = {1, 2, 3, 4}
>>> type(num1)
<class 'set'>
>>> num1{11,2,1,211,2,1,3,4,5,5,3}
SyntaxError: invalid syntax
>>> num1 = {11,2,1,211,2,1,3,4,5,5,3}
>>> num1
{1, 2, 3, 4, 5, 11, 211}
>>> num1[2]
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    num1[2]
TypeError: 'set' object does not support indexing
>>> num3 = set([1, 2, 3, 4, 5, 5, 4])
>>> num3
{1, 2, 3, 4, 5}
>>> list[0, 1, 2, 3, 4, 0, 2, 4, 5]
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    list[0, 1, 2, 3, 4, 0, 2, 4, 5]
TypeError: 'type' object is not subscriptable
>>> list = [0, 1, 2, 3, 4, 0, 2, 4, 5]
>>> temp = []
>>> for each in list:
	if each not in temp:
		temp.append(each)

		
>>> temp
[0, 1, 2, 3, 4, 5]
>>> num1 = list(set(list))
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    num1 = list(set(list))
TypeError: 'list' object is not callable
>>> list
[0, 1, 2, 3, 4, 0, 2, 4, 5]
>>> num1 = list(set(num1))
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    num1 = list(set(num1))
TypeError: 'list' object is not callable
>>> num1 = list(set(list))
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    num1 = list(set(list))
TypeError: 'list' object is not callable
>>> num1 = list
>>> num1 = list(set(num1))
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    num1 = list(set(num1))
TypeError: 'list' object is not callable
>>> num1
[0, 1, 2, 3, 4, 0, 2, 4, 5]
>>> num1 = list(set(num1))
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    num1 = list(set(num1))
TypeError: 'list' object is not callable
>>> num1 = set(num1)
>>> num1
{0, 1, 2, 3, 4, 5}
>>> num1 = list(num1)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    num1 = list(num1)
TypeError: 'list' object is not callable
>>> num1
{0, 1, 2, 3, 4, 5}
>>> num1 = list(num1)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    num1 = list(num1)
TypeError: 'list' object is not callable
>>> num2 = frozenset(num1)
>>> num2
frozenset({0, 1, 2, 3, 4, 5})
>>> num2.appand(6)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    num2.appand(6)
AttributeError: 'frozenset' object has no attribute 'appand'
>>> num1.append(6)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    num1.append(6)
AttributeError: 'set' object has no attribute 'append'
>>> num1
{0, 1, 2, 3, 4, 5}
>>> num1.add(6)
>>> num1
{0, 1, 2, 3, 4, 5, 6}
>>> num2.add(6)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    num2.add(6)
AttributeError: 'frozenset' object has no attribute 'add'
>>> 
