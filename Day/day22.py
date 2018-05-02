Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def foo(s):
	n = int(s)
	print('>>> n = %d' % n)
	return 10 / n

>>> def main():
	foo('0')

	
>>> main()
>>> n = 0
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    main()
  File "<pyshell#7>", line 2, in main
    foo('0')
  File "<pyshell#4>", line 4, in foo
    return 10 / n
ZeroDivisionError: division by zero
>>> def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

>>> main()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    main()
  File "<pyshell#7>", line 2, in main
    foo('0')
  File "<pyshell#10>", line 3, in foo
    assert n != 0, 'n is zero!'
AssertionError: n is zero!
>>> import logging

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
SyntaxError: multiple statements found while compiling a single statement
>>> import logging
>>> s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
SyntaxError: multiple statements found while compiling a single statement
>>> 
