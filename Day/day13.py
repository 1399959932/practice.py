Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> L = [x * x for x in range(10)]
>>> L
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> G = (x * x for x in range(10))
>>> G
<generator object <genexpr> at 0x02F3A8D0>
>>> next(G)
0
>>> next(G)
1
>>> next(G)
4
>>> next(G)
9
>>> next(G)
16
>>> g = (x * x for x in range(10))
>>> for i in g:
	print(i)

	
0
1
4
9
16
25
36
49
64
81
>>> def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		print(b)
		a, b = b, a + b
		n = n + 1
	return 'done'

>>> fib(6)
1
1
2
3
5
8
'done'
>>> 
