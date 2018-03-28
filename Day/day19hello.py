Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 

>>> 
>>> class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

        
>>> f = Fib()
>>> f[0:6]
[1, 1, 2, 3, 5, 8]
>>> f[:6]
[1, 1, 2, 3, 5, 8]
>>> f[:10:2]
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
>>> class Student(object):
	def __init__(self):
		self.name = 'Ronin Chen'

		
>>> s = Student()
>>> s.name
'Ronin Chen'
>>> print(s.name)
Ronin Chen
>>> print(s.sorce)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(s.sorce)
AttributeError: 'Student' object has no attribute 'sorce'
>>> class Student(object):
	def __init__(self):
		self.name = 'Ronin Chen'
	def __getattr__(self, attr):
		if attr=='score'
		
SyntaxError: invalid syntax
>>> class Student(object):
	def __init__(self):
		self.name = 'Ronin Chen'
	def __getattr__(self, attr):
		if attr=='score':
			return 99

		
>>> s = Student()
>>> print(s.score)
99
>>> print(s.scores)
None
>>> s.score()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    s.score()
TypeError: 'int' object is not callable
>>> class Student(object):

    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25

        
>>> 
>>> 
>>> 
>>> s.age()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    s.age()
TypeError: 'NoneType' object is not callable
>>> s = Student()
>>> s.age()
25
>>> class Student(object):

    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

>>> s = Student()
>>> s.age()
25
>>> s.ages()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    s.ages()
  File "<pyshell#35>", line 6, in __getattr__
    raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
AttributeError: 'Student' object has no attribute 'ages'
>>> class Student(object):

    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25

        
>>> s = Student()
>>> s.age
<function Student.__getattr__.<locals>.<lambda> at 0x02FD1B70>
>>> s.age()
25
>>> s.ages()
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    s.ages()
TypeError: 'NoneType' object is not callable
>>> class Chanin(object):
	def __init__(self, path=''):
		self._path = path
	def __getattr__(self, path):
		return Chain('%s/%s' % (self._path, path))
	def __str__(self):
		return self.path
	__repr__ = __str__

	
>>> Chain().status.user.timeline.list
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    Chain().status.user.timeline.list
NameError: name 'Chain' is not defined
>>> Chain().status.user.timeline.list
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    Chain().status.user.timeline.list
NameError: name 'Chain' is not defined
>>> class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

    
>>> Chain().status.user.timeline.list
/status/user/timeline/list
>>> class Chain(object):

	    def __init__(self, path=''):
		self._path = path
	
	    def __getattr__(self, path):
	        return Chain('%s/%s' % (self._path, path))

	    def __str__(self):
	        return self._path

	    __repr__ = __str__
	    
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> 
>>> class Chain(object):

	    def __init__(self, path=''):
	self._path = path
	
	    def __getattr__(self, path):
	        return Chain('%s/%s' % (self._path, path))

	    def __str__(self):
	        return self._path

	    __repr__ = __str__
	    
SyntaxError: unindent does not match any outer indentation level
>>> 
>>> GET /users/:user/repos
SyntaxError: invalid syntax
>>> GET /users/:user/repos
SyntaxError: invalid syntax
>>> Chain().users('michael').repos
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    Chain().users('michael').repos
TypeError: 'Chain' object is not callable
>>> class Student(object):
	def __init__(self, name):
		self.name = name
	def __call__(self):
		print('My name is %s.' % self.name)

		
>>> s = Student()
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    s = Student()
TypeError: __init__() missing 1 required positional argument: 'name'
>>> s = Student('Ronin Chen')
>>> s()
My name is Ronin Chen.
>>> callable(s())
My name is Ronin Chen.
False
>>> callable(s)
True
>>> callable('str')
False
>>> callable(Student())
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    callable(Student())
TypeError: __init__() missing 1 required positional argument: 'name'
>>> callable(Student())
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    callable(Student())
TypeError: __init__() missing 1 required positional argument: 'name'
>>> 
>>> 
>>> 
>>> from enum import Enum
>>> Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
>>> for name, member in Month.__members__.items():
	print(name, '=>', member, ',', member.value)

	
Jan => Month.Jan , 1
Feb => Month.Feb , 2
Mar => Month.Mar , 3
Apr => Month.Apr , 4
May => Month.May , 5
Jun => Month.Jun , 6
Jul => Month.Jul , 7
Aug => Month.Aug , 8
Sep => Month.Sep , 9
Oct => Month.Oct , 10
Nov => Month.Nov , 11
Dec => Month.Dec , 12
>>> form enum import Eunm, unique
SyntaxError: invalid syntax
>>> from enum import Eunm, unique
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    from enum import Eunm, unique
ImportError: cannot import name 'Eunm'
>>> from enum import Enum, unique
>>> @unique
class Weekdat(Enum):
	Sun = 0
	Mon = 1
	Tue = 2
	Web = 3
	Thu = 4
	Fri = 5
	Sat = 6

	
>>> day1 = Weekday.Mon
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    day1 = Weekday.Mon
NameError: name 'Weekday' is not defined
>>> @unique
class Weekday(Enum):
	Sun = 0
	Mon = 1
	Tue = 2
	Web = 3
	Thu = 4
	Fri = 5
	Sat = 6

	
>>> day1 = Weekday.Mon
>>> print(day1)
Weekday.Mon
>>> print(Weekdat.Tue)
Weekdat.Tue
>>> print(Weekdat[Tue])
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    print(Weekdat[Tue])
NameError: name 'Tue' is not defined
>>> print(Weekdat['Tue'])
Weekdat.Tue
>>> print(Weekdat.Tue.value)
2
>>> print(day1 == Weekday.Mon)
True
>>> print(Weekdat(1))
Weekdat.Mon
>>> print(Weekdat(7))
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    print(Weekdat(7))
  File "C:\Users\JK-chenxs\AppData\Local\Programs\Python\Python36-32\lib\enum.py", line 291, in __call__
    return cls.__new__(cls, value)
  File "C:\Users\JK-chenxs\AppData\Local\Programs\Python\Python36-32\lib\enum.py", line 533, in __new__
    return cls._missing_(value)
  File "C:\Users\JK-chenxs\AppData\Local\Programs\Python\Python36-32\lib\enum.py", line 546, in _missing_
    raise ValueError("%r is not a valid %s" % (value, cls.__name__))
ValueError: 7 is not a valid Weekdat
>>> for name, member in Weekday.__member__.items():
	print(name, '=>', member)

	
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    for name, member in Weekday.__member__.items():
  File "C:\Users\JK-chenxs\AppData\Local\Programs\Python\Python36-32\lib\enum.py", line 320, in __getattr__
    raise AttributeError(name)
AttributeError: __member__
>>> for name, member in Weekday.__members__.items():
	 print(name, '=>', member)

	 
Sun => Weekday.Sun
Mon => Weekday.Mon
Tue => Weekday.Tue
Web => Weekday.Web
Thu => Weekday.Thu
Fri => Weekday.Fri
Sat => Weekday.Sat
>>> class Hello(object):
	def hello(self, name='world'):
		print('Hello, %s.' % name)

		
>>> from hello import Hello
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    from hello import Hello
ModuleNotFoundError: No module named 'hello'
>>> from hello import day19hello
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    from hello import day19hello
ModuleNotFoundError: No module named 'hello'
>>> from hello import day19hello
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    from hello import day19hello
ModuleNotFoundError: No module named 'hello'
>>> from hello import Hello
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    from hello import Hello
ModuleNotFoundError: No module named 'hello'
>>> 
