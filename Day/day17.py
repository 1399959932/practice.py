Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 

>>> class Student(object):
	pass

>>> bart = Student
>>> bart = Student()
>>> bart
<__main__.Student object at 0x0048AC30>
>>> bart = Student
>>> bart
<class '__main__.Student'>
>>> bart = Student()
>>> bart
<__main__.Student object at 0x0048AC30>
>>> student
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    student
NameError: name 'student' is not defined
>>> Student
<class '__main__.Student'>
>>> bart.name = 'Ronin Chen'
>>> bart.name
'Ronin Chen'
>>> class Student(object):
	def __init__(self, name, score):
		self.name = name
		self.score = score

		
>>> bart = Student('Bart Simpson')
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    bart = Student('Bart Simpson')
TypeError: __init__() missing 1 required positional argument: 'score'
>>> bart = Student('Ronin Chen', 99)
>>> bart.name
'Ronin Chen'
>>> bart.score
99
>>> def print_score(std):
	print('%s: %s' % (std.name, std.score))

	
>>> print_score(bart)
Ronin Chen: 99
>>> class Student(object):

	    def __init__(self, name, score):
		self.name = name
		self.score = score

	    def print_score(self):
	        print('%s: %s' % (self.name, self.score))
	        
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> class Student(object):

	    def __init__(self, name, score):
		self.name = name
		self.score = score

	    def print_score(self):
	        print('%s: %s' % (self.name, self.score))
	        
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> class Student(object):

	def __init__(self, name, score):
		self.name = name
		self.score = score

	def print_score(self):
	        print('%s: %s' % (self.name, self.score))

	        
>>> bart.print_score()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    bart.print_score()
AttributeError: 'Student' object has no attribute 'print_score'
>>> bart.print_score()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    bart.print_score()
AttributeError: 'Student' object has no attribute 'print_score'
>>> bart.print_score('')
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    bart.print_score('')
AttributeError: 'Student' object has no attribute 'print_score'
>>> bart
<__main__.Student object at 0x02F23C50>
>>> bart()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    bart()
TypeError: 'Student' object is not callable
>>> bart.name
'Ronin Chen'
>>> bart.print_score()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    bart.print_score()
AttributeError: 'Student' object has no attribute 'print_score'
>>> bart.print_score
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    bart.print_score
AttributeError: 'Student' object has no attribute 'print_score'
>>> bart.print_score()
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    bart.print_score()
AttributeError: 'Student' object has no attribute 'print_score'
>>> class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

        
>>> bart.print_score()
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    bart.print_score()
AttributeError: 'Student' object has no attribute 'print_score'
>>> bart.print_score()
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    bart.print_score()
AttributeError: 'Student' object has no attribute 'print_score'
>>> bart.print_score()
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    bart.print_score()
AttributeError: 'Student' object has no attribute 'print_score'
>>> class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

        
>>> bart.print_score()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    bart.print_score()
AttributeError: 'Student' object has no attribute 'print_score'
>>> class Student(object):
    ...

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

        
>>> bart.get_grade()
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    bart.get_grade()
AttributeError: 'Student' object has no attribute 'get_grade'
>>> bart.name
'Ronin Chen'
>>> bart.score
99
>>> class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

        
>>> bart.get_grade()
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    bart.get_grade()
AttributeError: 'Student' object has no attribute 'get_grade'
>>> class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

        
>>> bart.print_score()
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    bart.print_score()
AttributeError: 'Student' object has no attribute 'print_score'
>>> def print_score(std):
	print('%s: %s' % (std.name, std.score))

	
>>> print_score(bart)
Ronin Chen: 99
>>> class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

        
>>> 
>>> bart.print_score()
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    bart.print_score()
AttributeError: 'Student' object has no attribute 'print_score'
>>> bart.__init__
<bound method Student.__init__ of <__main__.Student object at 0x02F23C50>>
>>> bart.__init__()
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    bart.__init__()
TypeError: __init__() missing 2 required positional arguments: 'name' and 'score'
>>> bart.__init__('陈', 66)
>>> bart.__init__()
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    bart.__init__()
TypeError: __init__() missing 2 required positional arguments: 'name' and 'score'
>>> bart.__init__
<bound method Student.__init__ of <__main__.Student object at 0x02F23C50>>
>>> bart.print_score()
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    bart.print_score()
AttributeError: 'Student' object has no attribute 'print_score'
>>> bart
<__main__.Student object at 0x02F23C50>
>>> bart.name
'陈'
>>> bart
<__main__.Student object at 0x02F23C50>
>>> print(bart)
<__main__.Student object at 0x02F23C50>
>>> print(bart())
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    print(bart())
TypeError: 'Student' object is not callable
>>> bart()
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    bart()
TypeError: 'Student' object is not callable
>>> bart.score
66
>>>  def print_score(std):
     print('%s: %s' % (std.name, std.score))
     
SyntaxError: unexpected indent
>>> def print_score(std):
     print('%s: %s' % (std.name, std.score))

     
>>> print_score()
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    print_score()
TypeError: print_score() missing 1 required positional argument: 'std'
>>> print_score(std)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    print_score(std)
NameError: name 'std' is not defined
>>> print_score('陈')
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    print_score('陈')
  File "<pyshell#83>", line 2, in print_score
    print('%s: %s' % (std.name, std.score))
AttributeError: 'str' object has no attribute 'name'
>>> class Student(object):
	pass

>>> Student
<class '__main__.Student'>
>>> print(Student)
<class '__main__.Student'>
>>> print('Student')
Student
>>> bart = Student()
>>> bart
<__main__.Student object at 0x02F37F50>
>>> Student
<class '__main__.Student'>
>>> bart.name = 'Ronin Chen'
>>> bart.name
'Ronin Chen'
>>> class Student(object):
	def __init__(self, name, score):
		self.name = name
		self.score = score

		
>>> bart = Student('陈', 66)
>>> bart.name
'陈'
>>> bart.score
66
>>> def print_score(std):
	print('%s: %s' % (std.name, std.score))

	
>>> print_score(bart)
陈: 66
>>> class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

        
>>> bart.print_score()
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    bart.print_score()
AttributeError: 'Student' object has no attribute 'print_score'
>>> class Student(object):
	def __init__(self, name, score):
		self.name = name
		self.score = score
	def print_score(self):
		print('%s: %s' % (self.name, self.score))

		
>>> bart.print_score()
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    bart.print_score()
AttributeError: 'Student' object has no attribute 'print_score'
>>> object.print_score()
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    object.print_score()
AttributeError: type object 'object' has no attribute 'print_score'
>>> bart.name
'陈'
>>> bart
<__main__.Student object at 0x02F23C50>
>>> bart.name = 'Bart Simpson'
>>> bart
<__main__.Student object at 0x02F23C50>
>>> bart.print_score()
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    bart.print_score()
AttributeError: 'Student' object has no attribute 'print_score'
>>> bart = Student('CHEN', 66)
>>> lisa = Student('chen', 88)
>>> bart.age = 8
>>> bart.age
8
>>> lisa.age
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    lisa.age
AttributeError: 'Student' object has no attribute 'age'
>>> lisa.age = 6
>>> lisa.age
6
>>> bart = Student('陈', 66)
>>> bart.score
66
>>> bart.score = 99
>>> bart.score
99
>>> bart
<__main__.Student object at 0x02FB16B0>
>>> class Student(object):
	def __init__(self, name, score):
		self.__name = name
		self.__score =  score

		
>>> class Student(object):
	def __init__(self, name, score):
		self.__name = name
		self.__score =  score
	def print_score(self):
		print('%s: %s' % (self.__name, self.__score))

		
>>> bart = Student('SSSS', 55)
>>> bart.__name
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    bart.__name
AttributeError: 'Student' object has no attribute '__name'
>>> class Student(object):
	def __init__(self, name, score):
		self.__name = name
		self.__score = score
	def print_score(self):
		print('%s: %s' % (self.__name, self.__score))

		
>>> class Student(object):
	def get_name(self):
		return self.__name
	def get_score(self):
		return self.__score

	
>>> bart.__name
Traceback (most recent call last):
  File "<pyshell#163>", line 1, in <module>
    bart.__name
AttributeError: 'Student' object has no attribute '__name'
>>> bart = Student('name', 6)
Traceback (most recent call last):
  File "<pyshell#164>", line 1, in <module>
    bart = Student('name', 6)
TypeError: object() takes no parameters
>>> class Student(object):
	def get_score(self, score):
		self.__score = score

		
>>> bart.get_name()
Traceback (most recent call last):
  File "<pyshell#168>", line 1, in <module>
    bart.get_name()
AttributeError: 'Student' object has no attribute 'get_name'
>>> bart.Student.get_name()
Traceback (most recent call last):
  File "<pyshell#169>", line 1, in <module>
    bart.Student.get_name()
AttributeError: 'Student' object has no attribute 'Student'
>>> Student.get_name()
Traceback (most recent call last):
  File "<pyshell#170>", line 1, in <module>
    Student.get_name()
AttributeError: type object 'Student' has no attribute 'get_name'
>>> class Student(object):
    ...

    def set_score(self, score):
        self.__score = score

        
>>>  class Student(object):
	def __init__(self, name, score):
		self.__name = name
		self.__score = score
	def print_score(self):
		print('%s: %s' % (self.__name, self.__score))
		
SyntaxError: unexpected indent
>>> class Student(object):
	def __init__(self, name, score):
		self.__name = name
		self.__score = score
	def print_score(self):
		print('%s: %s' % (self.__name, self.__score))

		
>>> class Student(object):
    ...

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

>>> bart.
SyntaxError: invalid syntax
>>> bart.print_score()
SSSS: 55
>>> bart.set_score(22)
Traceback (most recent call last):
  File "<pyshell#180>", line 1, in <module>
    bart.set_score(22)
AttributeError: 'Student' object has no attribute 'set_score'
>>> bart.__name = 66
>>> bart.__name
66
>>> bart.__score
Traceback (most recent call last):
  File "<pyshell#183>", line 1, in <module>
    bart.__score
AttributeError: 'Student' object has no attribute '__score'
>>> bart.score
Traceback (most recent call last):
  File "<pyshell#184>", line 1, in <module>
    bart.score
AttributeError: 'Student' object has no attribute 'score'
>>> bart.name
Traceback (most recent call last):
  File "<pyshell#185>", line 1, in <module>
    bart.name
AttributeError: 'Student' object has no attribute 'name'
>>> bart.__name
66
>>> bart.__name =  45
>>> bart.__name
45
>>> bart.__score
Traceback (most recent call last):
  File "<pyshell#189>", line 1, in <module>
    bart.__score
AttributeError: 'Student' object has no attribute '__score'
>>> class Student(object):
	...

	
>>> class Student(object):
	...
	def set_score(self, score):
		if 0 <= score <= 100:
			self.__score = score
		else:
			raise ValueError('bad score')

		
>>> bart.__score = 101
>>> bart.__score
101
>>> bart.__name = 101
>>> bart.name
Traceback (most recent call last):
  File "<pyshell#203>", line 1, in <module>
    bart.name
AttributeError: 'Student' object has no attribute 'name'
>>> bart.__name
101
>>> bart.print_score()
SSSS: 55
>>> bart.ger_mame
Traceback (most recent call last):
  File "<pyshell#206>", line 1, in <module>
    bart.ger_mame
AttributeError: 'Student' object has no attribute 'ger_mame'
>>> bart.get_mame
Traceback (most recent call last):
  File "<pyshell#207>", line 1, in <module>
    bart.get_mame
AttributeError: 'Student' object has no attribute 'get_mame'
>>> bart.get_mame()
Traceback (most recent call last):
  File "<pyshell#208>", line 1, in <module>
    bart.get_mame()
AttributeError: 'Student' object has no attribute 'get_mame'
>>> bart.get_mame(55)
Traceback (most recent call last):
  File "<pyshell#209>", line 1, in <module>
    bart.get_mame(55)
AttributeError: 'Student' object has no attribute 'get_mame'
>>> bart.Student.get_mame(55)
Traceback (most recent call last):
  File "<pyshell#210>", line 1, in <module>
    bart.Student.get_mame(55)
AttributeError: 'Student' object has no attribute 'Student'
>>> Student.get_mame(bart)
Traceback (most recent call last):
  File "<pyshell#211>", line 1, in <module>
    Student.get_mame(bart)
AttributeError: type object 'Student' has no attribute 'get_mame'
>>> Student.get_mame('bart')
Traceback (most recent call last):
  File "<pyshell#212>", line 1, in <module>
    Student.get_mame('bart')
AttributeError: type object 'Student' has no attribute 'get_mame'
>>> bart.get_name(Student)
Traceback (most recent call last):
  File "<pyshell#213>", line 1, in <module>
    bart.get_name(Student)
AttributeError: 'Student' object has no attribute 'get_name'
>>> bart.get_name('Student')
Traceback (most recent call last):
  File "<pyshell#214>", line 1, in <module>
    bart.get_name('Student')
AttributeError: 'Student' object has no attribute 'get_name'
>>> bart._studnet_get_name('Student')
Traceback (most recent call last):
  File "<pyshell#215>", line 1, in <module>
    bart._studnet_get_name('Student')
AttributeError: 'Student' object has no attribute '_studnet_get_name'
>>> bart._studnet_get_name('qs')
Traceback (most recent call last):
  File "<pyshell#216>", line 1, in <module>
    bart._studnet_get_name('qs')
AttributeError: 'Student' object has no attribute '_studnet_get_name'
>>> bart._studnet.get_name('qs')
Traceback (most recent call last):
  File "<pyshell#217>", line 1, in <module>
    bart._studnet.get_name('qs')
AttributeError: 'Student' object has no attribute '_studnet'
>>> bart._Student__name
'SSSS'
>>> bart = Student('Ronin Chen', 59)
Traceback (most recent call last):
  File "<pyshell#219>", line 1, in <module>
    bart = Student('Ronin Chen', 59)
TypeError: object() takes no parameters
>>> bart.get_name()
Traceback (most recent call last):
  File "<pyshell#220>", line 1, in <module>
    bart.get_name()
AttributeError: 'Student' object has no attribute 'get_name'
>>> class Student(object):
    ...

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

>>> bart.get_name()
Traceback (most recent call last):
  File "<pyshell#223>", line 1, in <module>
    bart.get_name()
AttributeError: 'Student' object has no attribute 'get_name'
>>> class Student(object):
    ...

	    def get_name(self):
	        return self.__name

	    def get_score(self):
	        return self.__score
	
SyntaxError: unexpected indent
>>> class Student(object):
	    ...

	def get_name(self):
		return self.__name

	    def get_score(self):
		return self.__score
	
SyntaxError: unindent does not match any outer indentation level
>>> class Student(object):
    ...

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

>>> bart.get_name()
Traceback (most recent call last):
  File "<pyshell#228>", line 1, in <module>
    bart.get_name()
AttributeError: 'Student' object has no attribute 'get_name'
>>> class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

        
>>> class Student(object):
    ...

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

>>> class Student(object):
    ...

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

        
>>> bart = Student('Ronin Chen', 66)
Traceback (most recent call last):
  File "<pyshell#235>", line 1, in <module>
    bart = Student('Ronin Chen', 66)
TypeError: object() takes no parameters
>>> bart.get_name()
Traceback (most recent call last):
  File "<pyshell#236>", line 1, in <module>
    bart.get_name()
AttributeError: 'Student' object has no attribute 'get_name'
>>> class Student(object):

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

>>> bart = Student('Ronin Chen', 66)
Traceback (most recent call last):
  File "<pyshell#239>", line 1, in <module>
    bart = Student('Ronin Chen', 66)
TypeError: object() takes no parameters
>>> class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

        
>>> bart.get_name()
Traceback (most recent call last):
  File "<pyshell#242>", line 1, in <module>
    bart.get_name()
AttributeError: 'Student' object has no attribute 'get_name'
>>> bart = Student('Ronin Chen', 66)
>>> bart.get_name()
'Ronin Chen'
>>> class Animal(object):
	def run(self):
		print('Animal is running')

		
>>> run()
Traceback (most recent call last):
  File "<pyshell#249>", line 1, in <module>
    run()
NameError: name 'run' is not defined
>>> Animal()
<__main__.Animal object at 0x02F37CF0>
>>> print(Animal())
<__main__.Animal object at 0x02F37BD0>
>>> class Dog(Animal):
	pass

>>> 
>>> class Cat(Animal):
	pass

>>> dog = Dog()
>>> dog.run()
Animal is running
>>> Animal.run()
Traceback (most recent call last):
  File "<pyshell#261>", line 1, in <module>
    Animal.run()
TypeError: run() missing 1 required positional argument: 'self'
>>> cat = s()
Traceback (most recent call last):
  File "<pyshell#262>", line 1, in <module>
    cat = s()
NameError: name 's' is not defined
>>> cat = Cat()
>>> cat.run()
Animal is running
>>> class Dog(Animal):
	def run(self):
		print('Dog is running...')
	def eat(self):
		print('Eating meat')

		
>>> class Dog(Animal):
	def run(self):
		print('Dog is running...')
	def eat(self):
		print('Eating meat')

		
>>> class Cat(Animal):
	def run(self):
		print('Cat is running.')

		
>>> Cat()
<__main__.Cat object at 0x02F37AB0>
>>> dog.run()
Animal is running
>>> cat.run()
Animal is running
>>> dog = Dog()
>>> dog.run()
Dog is running...
>>> cat = Cat()
>>> cat
<__main__.Cat object at 0x02F37690>
>>> cat()
Traceback (most recent call last):
  File "<pyshell#285>", line 1, in <module>
    cat()
TypeError: 'Cat' object is not callable
>>> cat.run()
Cat is running.
>>> dog.eat()
Eating meat
>>> def run_twice(animal):
	animal.run()
	animal.run()

	
>>> run_twice(run())
Traceback (most recent call last):
  File "<pyshell#292>", line 1, in <module>
    run_twice(run())
NameError: name 'run' is not defined
>>> run_twice(Animal())
Animal is running
Animal is running
>>> run_twice(Dog())
Dog is running...
Dog is running...
>>> run_twice(Cat())
Cat is running.
Cat is running.
>>> class Tortoise(Animal):
	def run(self):
		print('Tortoise is running slowly.')

		
>>> run_twice(Tortoise())
Tortoise is running slowly.
Tortoise is running slowly.
>>> class Timer(object):
	def run(self):
		print('Start...')

		
>>> dog.run)_
SyntaxError: invalid syntax
>>> dog.run()
Dog is running...
>>> Timer.run)_
SyntaxError: invalid syntax
>>> Timer.run()
Traceback (most recent call last):
  File "<pyshell#308>", line 1, in <module>
    Timer.run()
TypeError: run() missing 1 required positional argument: 'self'
>>> timer = Timer()
>>> timer.run()
Start...
>>> timer = Animal()
>>> timer.run()
Animal is running
>>> timer.eat()
Traceback (most recent call last):
  File "<pyshell#313>", line 1, in <module>
    timer.eat()
AttributeError: 'Animal' object has no attribute 'eat'
>>> timer = eat()
Traceback (most recent call last):
  File "<pyshell#314>", line 1, in <module>
    timer = eat()
NameError: name 'eat' is not defined
>>> timer = cat()
Traceback (most recent call last):
  File "<pyshell#315>", line 1, in <module>
    timer = cat()
TypeError: 'Cat' object is not callable
>>> timer = dog()
Traceback (most recent call last):
  File "<pyshell#316>", line 1, in <module>
    timer = dog()
TypeError: 'Dog' object is not callable
>>> timer = dog()
Traceback (most recent call last):
  File "<pyshell#317>", line 1, in <module>
    timer = dog()
TypeError: 'Dog' object is not callable
>>> 
>>> type(123)==type(321)
True
>>> type(123)==int
True
>>> type(123)==type('12')
False
>>> type('55')==str
True
>>> import types
>>> def fn():
	pass

>>> type(fn)==type.FunctionType
Traceback (most recent call last):
  File "<pyshell#327>", line 1, in <module>
    type(fn)==type.FunctionType
AttributeError: type object 'type' has no attribute 'FunctionType'
>>> type(fn)==types.FunctionType
True
>>> type(abs)==types.FunctionType
False
>>> type(abs)==types.BuiltinFunctionType
True
>>> type(lambda x: x)==types.LamdbaType
Traceback (most recent call last):
  File "<pyshell#331>", line 1, in <module>
    type(lambda x: x)==types.LamdbaType
AttributeError: module 'types' has no attribute 'LamdbaType'
>>> type(lambda x: x)==types.LambdaType
True
>>> type((x for x in range(10)))===types.GeneratorType
SyntaxError: invalid syntax
>>> type((x for x in range(10)))==types.GeneratorType
True
>>> a = Animal)_
SyntaxError: invalid syntax
>>> a = Animal()
>>> b = dog()
Traceback (most recent call last):
  File "<pyshell#337>", line 1, in <module>
    b = dog()
TypeError: 'Dog' object is not callable
>>> b = Dog()
>>> c = Husky()
Traceback (most recent call last):
  File "<pyshell#339>", line 1, in <module>
    c = Husky()
NameError: name 'Husky' is not defined
>>> class  Husky(dog):
	def run(self):
		print('the dog is Husky')

		
Traceback (most recent call last):
  File "<pyshell#343>", line 1, in <module>
    class  Husky(dog):
TypeError: object() takes no parameters
>>> class  Husky(dog):
	def run(self):
		print('the dog is Husky')

		
Traceback (most recent call last):
  File "<pyshell#345>", line 1, in <module>
    class  Husky(dog):
TypeError: object() takes no parameters
>>> class  Husky(Animal):
	def run(self):
		print('the dog is Husky')

		
>>> isinstance(h, Husky)
Traceback (most recent call last):
  File "<pyshell#348>", line 1, in <module>
    isinstance(h, Husky)
NameError: name 'h' is not defined
>>> isinstance(c, Husky)
Traceback (most recent call last):
  File "<pyshell#349>", line 1, in <module>
    isinstance(c, Husky)
NameError: name 'c' is not defined
>>> c = Husky()
>>> isinstance(c, Husky)
True
>>> isinstance(c, Dog)
False
>>> class  Husky(Dog):
	def run(self):
		print('the dog is Husky')

		
>>> isinstance(c, Dog)
False
>>> c = Husky()
>>> isinstance(c, Dog)
True
>>> class  Husky(dog):
	def run(self):
		print('the dog is Husky')

		
Traceback (most recent call last):
  File "<pyshell#359>", line 1, in <module>
    class  Husky(dog):
TypeError: object() takes no parameters
>>> 
>>> isinstance(d, Dog) and isinstance(d, Animal)
Traceback (most recent call last):
  File "<pyshell#361>", line 1, in <module>
    isinstance(d, Dog) and isinstance(d, Animal)
NameError: name 'd' is not defined
>>> isinstance(b, Dog) and isinstance(b, Animal)
True
>>> isinstance(b, Husky)
False
>>> isinstance([1, 2, 3], (list, tuple))
True
>>> isinstance([1, 2, 3], (tuple, list))
True
>>> dir('ABC')
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> len('ASC')
3
>>> 'ASC'.__len__()
3
>>> class Mymymy(object):
	def __len__(self):
		return 'Mymymy'

	
>>> my = Mymymy()
>>> len(my)
Traceback (most recent call last):
  File "<pyshell#374>", line 1, in <module>
    len(my)
TypeError: 'str' object cannot be interpreted as an integer
>>> class Mydog(object):
	def __len__(self):
		return '100'

	
>>> dog = Mydog()
>>> len(dog)
Traceback (most recent call last):
  File "<pyshell#378>", line 1, in <module>
    len(dog)
TypeError: 'str' object cannot be interpreted as an integer
>>> class Mydog(object):
	def __len__(self):
		return mymymy

	
>>> my = Mymymy()
>>> len(my)
Traceback (most recent call last):
  File "<pyshell#382>", line 1, in <module>
    len(my)
TypeError: 'str' object cannot be interpreted as an integer
>>> class Mydog(object):
	def __len__(self):
		return 10

	
>>> my = Mymymy()
>>> len(my)
Traceback (most recent call last):
  File "<pyshell#386>", line 1, in <module>
    len(my)
TypeError: 'str' object cannot be interpreted as an integer
>>> class Mymymy(object):
	def __len__(self):
		return 100

	
>>> my = Mymymy()
>>> len(my)
100
>>> SSSSSSS'
SyntaxError: EOL while scanning string literal
>>> 'SSSSSSS'.lower()
'sssssss'
>>> lower('SSSSS')
Traceback (most recent call last):
  File "<pyshell#393>", line 1, in <module>
    lower('SSSSS')
NameError: name 'lower' is not defined
>>> class MyObject(object):
	def __init__(self):
		self.x = 9
	def power(self):
		return self.x * self.x

	
>>> obj = MyObject()
>>> obj(ss)
Traceback (most recent call last):
  File "<pyshell#401>", line 1, in <module>
    obj(ss)
NameError: name 'ss' is not defined
>>> hasattr(obj, 'x')
True
>>> obj.x
9
>>> obj.ss
Traceback (most recent call last):
  File "<pyshell#404>", line 1, in <module>
    obj.ss
AttributeError: 'MyObject' object has no attribute 'ss'
>>> obj.q
Traceback (most recent call last):
  File "<pyshell#405>", line 1, in <module>
    obj.q
AttributeError: 'MyObject' object has no attribute 'q'
>>> hasattr(obj, 'y')
False
>>> hasattr(obj, 'y', 19)
Traceback (most recent call last):
  File "<pyshell#407>", line 1, in <module>
    hasattr(obj, 'y', 19)
TypeError: hasattr expected 2 arguments, got 3
>>> setattr(obj, 'y', 19)
>>> setattr(obj, 'y')
Traceback (most recent call last):
  File "<pyshell#409>", line 1, in <module>
    setattr(obj, 'y')
TypeError: setattr expected 3 arguments, got 2
>>> hasattr(obj, 'y')
True
>>> getattr(obj, 'q')
Traceback (most recent call last):
  File "<pyshell#411>", line 1, in <module>
    getattr(obj, 'q')
AttributeError: 'MyObject' object has no attribute 'q'
>>> getattr(obj, 'z', 404)
404
>>> hasattr(obj, 'power')
True
>>> getattr(obj, 'power')
<bound method MyObject.power of <__main__.MyObject object at 0x02FC3410>>
>>> fn = getattr(obj, 'power')
>>> fn
<bound method MyObject.power of <__main__.MyObject object at 0x02FC3410>>
>>> fn()
81
>>> sum  = obj.x + obj.y
>>> sum = getattr(obj, 'x') + getattr(obj, 'y')
>>> def readImage(fp):
	if haiattr(fp, 'read')
	
SyntaxError: invalid syntax
>>> def readImage(fp):
	if haiattr(fp, 'read'):
		return readData(fp)
	return None

>>> class Student(object):
	def __init__(self, name):
		self.name = name

		
>>> s= Student('BOb')
>>> s.score = 90
>>> class Student(object):
	name = 'Student'

	
>>> s = Student()
>>> print(s.name)
Student
>>> print(Student.name)
Student
>>> s.name = 'Ronin Chen'
>>> print(Student.name)
Student
>>> print(s.name)
Ronin Chen
>>> del s.name
>>> print(s.name)
Student
>>> class Student(object):
    count = 0
    count1 = [0]
    def init(self, name):
        self.name = name
        Student.count += 1
        self.count +=1
        Student.count1[0] += 1
        self.count1[0] += 1

        
>>> 
 RESTART: C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day17p.py 
Traceback (most recent call last):
  File "C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day17p.py", line 14, in <module>
    bart = Student('Bart')
TypeError: object() takes no parameters
>>> 
 RESTART: C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day17p.py 
Traceback (most recent call last):
  File "C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day17p.py", line 14, in <module>
    bart = Student('Bart')
TypeError: object() takes no parameters
>>> 
 RESTART: C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day17p.py 
>>> a = Student('a')
Traceback (most recent call last):
  File "<pyshell#445>", line 1, in <module>
    a = Student('a')
TypeError: object() takes no parameters
>>> 
