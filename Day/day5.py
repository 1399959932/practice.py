Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> range(5)
range(0, 5)
>>> 

>>> list(range(5))
[0, 1, 2, 3, 4]
>>> a = 1
>>> a
1
>>> for i in list(range(6))
SyntaxError: invalid syntax
>>> for i in list(range(6)):
	print(i)

	
0
1
2
3
4
5
>>> for i in range(2, 9):
	print(i)

	
2
3
4
5
6
7
8
>>> for i in range(1, 10, 2):
	print(i)

	
1
3
5
7
9
>>> bingo = '陈老爷'
want = input('你叫我什么:')
while True:
	if want == bingo:
		break
	want = input('我不是:')
print('以后请叫我陈老爷')
print('不要问我为什么')
SyntaxError: multiple statements found while compiling a single statement
>>> range(10)
range(0, 10)
>>> help(range)
Help on class range in module builtins:

class range(object)
 |  range(stop) -> range object
 |  range(start, stop[, step]) -> range object
 |  
 |  Return an object that produces a sequence of integers from start (inclusive)
 |  to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
 |  start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
 |  These are exactly the valid indices for a list of 4 elements.
 |  When step is given, it specifies the increment (or decrement).
 |  
 |  Methods defined here:
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __reduce__(...)
 |      helper for pickle
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(...)
 |      Return a reverse iterator.
 |  
 |  count(...)
 |      rangeobject.count(value) -> integer -- return number of occurrences of value
 |  
 |  index(...)
 |      rangeobject.index(value, [start, [stop]]) -> integer -- return index of value.
 |      Raise ValueError if the value is not present.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  start
 |  
 |  step
 |  
 |  stop

>>> dd = [1, 2, 3]
>>> dd
[1, 2, 3]
>>> del dd.[0]
SyntaxError: invalid syntax
>>> del dd[0]
>>> dd
[2, 3]
>>> dd.append(4)
>>> dd.append(5)
>>> dd
[2, 3, 4, 5]
>>> dd[1:3]
[3, 4]
>>> dd[0:3]
[2, 3, 4]
>>> d = dd[1:3]
>>> d
[3, 4]
>>> dd
[2, 3, 4, 5]
>>> dd *= 2
>>> dd
[2, 3, 4, 5, 2, 3, 4, 5]
>>> dd /= 2
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    dd /= 2
TypeError: unsupported operand type(s) for /=: 'list' and 'int'
>>> 2 in dd
True
>>> 2,3 in dd
(2, True)
>>> 2,2 in dd
(2, True)
>>> 6 not in dd
True
>>> 6 in dd
False
>>> dd.append('ss')
>>> dd
[2, 3, 4, 5, 2, 3, 4, 5, 'ss']
>>> ss in dd
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    ss in dd
NameError: name 'ss' is not defined
>>> 'ss' in dd
True
>>> 'ss' in dd[]
SyntaxError: invalid syntax
>>> 'ss' in dd[8]
True
>>> 'ss' in dd[4]
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    'ss' in dd[4]
TypeError: argument of type 'int' is not iterable
>>> dd[8]
'ss'
>>> dd[4]
2
>>> dd.count(2)
2
>>> dd.count(ss)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    dd.count(ss)
NameError: name 'ss' is not defined
>>> dd.count('ss')
1
>>> dd.severse()
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    dd.severse()
AttributeError: 'list' object has no attribute 'severse'
>>> dd.reverse()
>>> dd
['ss', 5, 4, 3, 2, 5, 4, 3, 2]
>>> list
