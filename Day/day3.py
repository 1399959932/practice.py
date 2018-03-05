Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> classmates = ['Micheal','Bob','JK-chenxs']
classmates

SyntaxError: multiple statements found while compiling a single statement
>>> classmates = ['Micheal','Bob','JK-chenxs']
>>> classmates
['Micheal', 'Bob', 'JK-chenxs']
>>> 

>>> len(classmates)
3
>>> classmates[0]
'Micheal'
>>> help(len)
Help on built-in function len in module builtins:

len(obj, /)
    Return the number of items in a container.

>>> classmates[1]
'Bob'
>>> classmates[2]
'JK-chenxs'
>>> classmates[-1]
'JK-chenxs'
>>> classmates.append('Admin')
>>> classmates
['Micheal', 'Bob', 'JK-chenxs', 'Admin']
>>> classmates.insert(2, 'goodboy')
>>> classmates
['Micheal', 'Bob', 'goodboy', 'JK-chenxs', 'Admin']
>>> classm
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    classm
NameError: name 'classm' is not defined
>>> classmates.pop()
'Admin'
>>> classmates.pop(2)
'goodboy'
>>> classmates
['Micheal', 'Bob', 'JK-chenxs']
>>> classmates[0] = 'China'
>>> classmates
['China', 'Bob', 'JK-chenxs']
>>> L = ['Apple', 123, true]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    L = ['Apple', 123, true]
NameError: name 'true' is not defined
>>> List = ['Apple', 123, true]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    List = ['Apple', 123, true]
NameError: name 'true' is not defined
>>> L = [123, true]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    L = [123, true]
NameError: name 'true' is not defined
>>>  L = ['Apple', 123, True]
 
SyntaxError: unexpected indent
>>> L = ['Apple', 123, True]
>>> L
['Apple', 123, True]
>>> S = ['123', True, ['goodboy', 'chenxusheng']]
>>> S
['123', True, ['goodboy', 'chenxusheng']]
>>> S = ['123', True, ['goodboy', 'chenxusheng'], l]
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    S = ['123', True, ['goodboy', 'chenxusheng'], l]
NameError: name 'l' is not defined
>>> S = ['123', True, ['goodboy', 'chenxusheng'], L]
>>> S
['123', True, ['goodboy', 'chenxusheng'], ['Apple', 123, True]]
>>> L[0]
'Apple'
>>> S[3][0]
'Apple'
>>> O = []
>>> O
[]
>>> len(O)
0
>>> class = ['Chen', 'Xu', 'Sheng']
SyntaxError: invalid syntax
>>> class = ('Chen', 'Xu', 'Sheng')
SyntaxError: invalid syntax
>>> classmates = ('Chen', 'Xu', 'Sheng')
>>> classmates[0]
'Chen'
>>> c = (1)
>>> c
1
>>> c[0]
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    c[0]
TypeError: 'int' object is not subscriptable
>>> c = (1,)
>>> c
(1,)
>>> c[0]
1
>>> tuple('a', 'b', ['c', 'd'])
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    tuple('a', 'b', ['c', 'd'])
TypeError: tuple() takes at most 1 argument (3 given)
>>> ss = tuple('a', 'b', ['c', 'd'])
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    ss = tuple('a', 'b', ['c', 'd'])
TypeError: tuple() takes at most 1 argument (3 given)
>>> ss = ('a', 'b', ['c', 'd'])
>>> ss
('a', 'b', ['c', 'd'])
>>> ss[2][0] = d
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    ss[2][0] = d
NameError: name 'd' is not defined
>>> ss[2][0] = 'd'
>>> ss[2][1] = 'c'
>>> ss
('a', 'b', ['d', 'c'])
>>> ss[2].append[6]
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    ss[2].append[6]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> ss[2].append(6)
>>> ss
('a', 'b', ['d', 'c', 6])
>>> L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
>>> print(L[0][1])
Google
>>> print(L[0][0])
Apple
>>> print(L[1][1])
Python
>>> print(L[2][2])
Lisa
>>> L = [
    ['apple', 'pink', 'blue'],
    ['eat', 'use', 'more']
    ]
>>> L
[['apple', 'pink', 'blue'], ['eat', 'use', 'more']]
>>> L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
>>> L
[['Apple', 'Google', 'Microsoft'], ['Java', 'Python', 'Ruby', 'PHP'], ['Adam', 'Bart', 'Lisa']]
>>> age = 20
if age >= 18;
	print('your age is', age)
	print('adult')
	
SyntaxError: multiple statements found while compiling a single statement
>>> age = 20
if age >= 18:
	print('your age is', age)
	print('adult')ge = 20
	
SyntaxError: multiple statements found while compiling a single statement
>>> age = 20
if age >= 18:
    print('your age is', age)
    print('adult')
    
SyntaxError: multiple statements found while compiling a single statement
>>> age = 20
if age >= 18:
    print('your age is', age)
    print('adult')
    
SyntaxError: multiple statements found while compiling a single statement
>>> age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
    
SyntaxError: multiple statements found while compiling a single statement
>>> 
 RESTART: C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day3_1.py 
kid
>>> 
 RESTART: C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day3_1.py 
kid
>>> 
 RESTART: C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day3_1.py 
birth: 12
Traceback (most recent call last):
  File "C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day3_1.py", line 3, in <module>
    if birth < 2000:
TypeError: '<' not supported between instances of 'str' and 'int'
>>> 
 RESTART: C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day3_1.py 
birth: 1998
Traceback (most recent call last):
  File "C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day3_1.py", line 3, in <module>
    if birth < 2000:
TypeError: '<' not supported between instances of 'str' and 'int'
>>> 
 RESTART: C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day3_1.py 
birth: 1998
00前
>>> 
 RESTART: C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day3_1.py 
birth: 2222
00后
>>> 
 RESTART: C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day3_1.py 
birth: s
Traceback (most recent call last):
  File "C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day3_1.py", line 2, in <module>
    birth = int(s)
ValueError: invalid literal for int() with base 10: 's'
>>> help(float)
Help on class float in module builtins:

class float(object)
 |  float(x) -> floating point number
 |  
 |  Convert a string or number to a floating point number, if possible.
 |  
 |  Methods defined here:
 |  
 |  __abs__(self, /)
 |      abs(self)
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __bool__(self, /)
 |      self != 0
 |  
 |  __divmod__(self, value, /)
 |      Return divmod(self, value).
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __float__(self, /)
 |      float(self)
 |  
 |  __floordiv__(self, value, /)
 |      Return self//value.
 |  
 |  __format__(...)
 |      float.__format__(format_spec) -> string
 |      
 |      Formats the float according to format_spec.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getformat__(...) from builtins.type
 |      float.__getformat__(typestr) -> string
 |      
 |      You probably don't want to use this function.  It exists mainly to be
 |      used in Python's test suite.
 |      
 |      typestr must be 'double' or 'float'.  This function returns whichever of
 |      'unknown', 'IEEE, big-endian' or 'IEEE, little-endian' best describes the
 |      format of floating point numbers used by the C type named by typestr.
 |  
 |  __getnewargs__(...)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __int__(self, /)
 |      int(self)
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mod__(self, value, /)
 |      Return self%value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __neg__(self, /)
 |      -self
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __pos__(self, /)
 |      +self
 |  
 |  __pow__(self, value, mod=None, /)
 |      Return pow(self, value, mod).
 |  
 |  __radd__(self, value, /)
 |      Return value+self.
 |  
 |  __rdivmod__(self, value, /)
 |      Return divmod(value, self).
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rfloordiv__(self, value, /)
 |      Return value//self.
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __round__(...)
 |      Return the Integral closest to x, rounding half toward even.
 |      When an argument is passed, work like built-in round(x, ndigits).
 |  
 |  __rpow__(self, value, mod=None, /)
 |      Return pow(value, self, mod).
 |  
 |  __rsub__(self, value, /)
 |      Return value-self.
 |  
 |  __rtruediv__(self, value, /)
 |      Return value/self.
 |  
 |  __setformat__(...) from builtins.type
 |      float.__setformat__(typestr, fmt) -> None
 |      
 |      You probably don't want to use this function.  It exists mainly to be
 |      used in Python's test suite.
 |      
 |      typestr must be 'double' or 'float'.  fmt must be one of 'unknown',
 |      'IEEE, big-endian' or 'IEEE, little-endian', and in addition can only be
 |      one of the latter two if it appears to match the underlying C reality.
 |      
 |      Override the automatic determination of C-level floating point type.
 |      This affects how floats are converted to and from binary strings.
 |  
 |  __str__(self, /)
 |      Return str(self).
 |  
 |  __sub__(self, value, /)
 |      Return self-value.
 |  
 |  __truediv__(self, value, /)
 |      Return self/value.
 |  
 |  __trunc__(...)
 |      Return the Integral closest to x between 0 and x.
 |  
 |  as_integer_ratio(...)
 |      float.as_integer_ratio() -> (int, int)
 |      
 |      Return a pair of integers, whose ratio is exactly equal to the original
 |      float and with a positive denominator.
 |      Raise OverflowError on infinities and a ValueError on NaNs.
 |      
 |      >>> (10.0).as_integer_ratio()
 |      (10, 1)
 |      >>> (0.0).as_integer_ratio()
 |      (0, 1)
 |      >>> (-.25).as_integer_ratio()
 |      (-1, 4)
 |  
 |  conjugate(...)
 |      Return self, the complex conjugate of any float.
 |  
 |  fromhex(...) from builtins.type
 |      float.fromhex(string) -> float
 |      
 |      Create a floating-point number from a hexadecimal string.
 |      >>> float.fromhex('0x1.ffffp10')
 |      2047.984375
 |      >>> float.fromhex('-0x1p-1074')
 |      -5e-324
 |  
 |  hex(...)
 |      float.hex() -> string
 |      
 |      Return a hexadecimal representation of a floating-point number.
 |      >>> (-0.1).hex()
 |      '-0x1.999999999999ap-4'
 |      >>> 3.14159.hex()
 |      '0x1.921f9f01b866ep+1'
 |  
 |  is_integer(...)
 |      Return True if the float is an integer.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  imag
 |      the imaginary part of a complex number
 |  
 |  real
 |      the real part of a complex number

>>> 'Hello, %s' % 'world'
'Hello, world'
>>> 'Hello, %sworld'
'Hello, %sworld'
>>> 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
'Hello, 小明, 成绩提升了 17.1%'
>>> 
 RESTART: C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day3_1.py 
请输入您去年成绩：60
请输入您本次成绩：70
您本次成绩为 70 去年成绩为 60 比去年提升了16.7 %
>>> 'abc %s' % 'abc'  '%s'
'abc abc%s'
>>> 0.000000000000000000000000000000454
4.54e-31
>>> True + False
1
>>> a = '520'
>>> b = int(b)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    b = int(b)
NameError: name 'b' is not defined
>>> b = int(a)
>>> b
520
>>> c = str(b)
>>> c
'520'
>>> d = float(b)
>>> d
520.0
>>> a = str(5e4)
>>> a
'50000.0'
>>> int(a)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    int(a)
ValueError: invalid literal for int() with base 10: '50000.0'
>>> b = int(a)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    b = int(a)
ValueError: invalid literal for int() with base 10: '50000.0'
>>> a
'50000.0'
>>> b = int('a')
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    b = int('a')
ValueError: invalid literal for int() with base 10: 'a'
>>> type(a)
<class 'str'>
>>> b = int(a)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    b = int(a)
ValueError: invalid literal for int() with base 10: '50000.0'
>>> b = str(a)
>>> a
'50000.0'
>>> 
a= 4
>>> a= 4
>>> a += 1
>>> a
5
>>> a
5
>>> a
5
>>> a = b = c = 4
>>> a
4
>>> b
4
>>> c
4
>>> d
520.0
>>> 3 // 2
1
>>> 6/2
3.0
>>> 6 / 2
3.0
>>> 6 // 2
3
>>> 5 % 2
1
>>> 2 ** 2
4
>>> 3 ** 3
27
>>> print('%.4f' % 3.1415926)
3.1416
>>> print('%2d-%02d' % (3, 1))
 3-01
>>> print('%2d-%02d' % (3, 6))
 3-06
>>> print('%2d-%02d' % (3, 56))
