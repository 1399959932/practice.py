Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import os
>>> print('Process (%s) start...' % os.getpid())
Process (11576) start...
>>> pid = os.fork()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    pid = os.fork()
AttributeError: module 'os' has no attribute 'fork'
>>> from multiprocessing import Process
>>> import os
>>> def run_proc(name):
	print('Run child process %s' (%s)...' % (name, os.getpid()))
	      
SyntaxError: invalid syntax
>>> def run_proc(name):
	print('Run child process %s (%s)...' % (name, os.getpid()))

	
>>> def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
    
SyntaxError: invalid syntax
>>> 
>>> def run_proc(name):
	print('Run child process %s (%s)...' % (name, os.getpid()))

	if __name__=='__main__':
	    print('Parent process %s.' % os.getpid())
	    p = Process(target=run_proc, args=('test',))
	    print('Child process will start.')
	    p.start()
	    p.join()
	    print('Child process end.')

	    
>>> from multiprocessing import Process
>>> import os
>>> def run_proc(name):
	print('Run child process %s (%s)...' % (name, os.getpid()))

	if __name__=='__main__':
	    print('Parent process %s.' % os.getpid())
	    p = Process(target=run_proc, args=('test',))
	    print('Child process will start.')
	    p.start()
	    p.join()
	    print('Child process end.')

	    
>>> import subprocess
>>> print('$ nslookup www.python.org')
$ nslookup www.python.org
>>> 
