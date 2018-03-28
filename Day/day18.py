Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class
SyntaxError: invalid syntax
>>> class Student(object):
	pass

>>> 
>>> a = Student()
>>> s.name = 'Michael'
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    s.name = 'Michael'
NameError: name 's' is not defined
>>> a.name = 'Michael'
>>> print(a.name)
Michael
>>> def set_age(self, age):
	self.age = age

	
>>> from types import MethodType
>>> s.set_age = MethodType(set_age, s)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    s.set_age = MethodType(set_age, s)
NameError: name 's' is not defined
>>> a.set_age = MethodType(set_age, a)
>>> a.set_age(21)
>>> a
<__main__.Student object at 0x004DAC30>
>>> a.age
21
>>> s2 = Student()
>>> s2.set_age(21)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    s2.set_age(21)
AttributeError: 'Student' object has no attribute 'set_age'
>>> def set_score(self, score):
	self.score = score

	
>>> Student.set_score = set_score
>>> s.set_score(66)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    s.set_score(66)
NameError: name 's' is not defined
>>> a.set_score(66)
>>> a.score
66
>>> s2.set_score(1)
>>> s2.score
1
>>> 
