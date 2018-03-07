Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 

>>> import sys
>>> sys.setrecursionlimit(10000)
>>> def recursion():
	return recursion()

>>> recursion()

=============================== RESTART: Shell ===============================
>>> sys.setrecursionlimit(10)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    sys.setrecursionlimit(10)
NameError: name 'sys' is not defined
>>> import sys
>>> sys.setrecursionlimit(10)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    sys.setrecursionlimit(10)
RecursionError: cannot set the recursion limit to 10 at the recursion depth 6: the limit is too low
>>> sys.setrecursionlimit(100)
>>> recursion()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    recursion()
NameError: name 'recursion' is not defined
>>> sys.setrecursionlimit(10000)
>>> def recursion(n):
	return n = n * (n + 1)
SyntaxError: invalid syntax
>>> def jiex(n):
	print(n = n * (n + 1))

	
>>> jiex(3)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    jiex(3)
  File "<pyshell#15>", line 2, in jiex
    print(n = n * (n + 1))
TypeError: 'n' is an invalid keyword argument for this function
>>> 
 RESTART: C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day9_阶乘.py 
请输入一个正整数:
Traceback (most recent call last):
  File "C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day9_阶乘.py", line 7, in <module>
    number = int(print('请输入一个正整数:'))
TypeError: int() argument must be a string, a bytes-like object or a number, not 'NoneType'
>>> 
 RESTART: C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day9_阶乘.py 
请输入一个正整数:
Traceback (most recent call last):
  File "C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day9_阶乘.py", line 7, in <module>
    number = int(print('请输入一个正整数:'))
TypeError: int() argument must be a string, a bytes-like object or a number, not 'NoneType'
>>> 
 RESTART: C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day9_阶乘.py 
请输入一个正整数:6
6 的阶乘是;6
>>> 
 RESTART: C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day9_阶乘.py 
请输入一个正整数:5
5 的阶乘是;120
>>> 
 RESTART: C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day9_阶乘(递归方式).py 
请输入一个正整数:5
5 的阶乘是;120
>>> 
 RESTART: C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day9_阶乘(递归方式).py 1
请输入一个正整数:1
1 的阶乘是;1
>>> 
 RESTART: C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day9_阶乘(递归方式).py 
请输入一个正整数:66
66 的阶乘是;544344939077443064003729240247842752644293064388798874532860126869671081148416000000000000000
>>> 
 RESTART: C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day9_阶乘(递归方式).py 
请输入一个正整数:10
10 的阶乘是;3628800
>>> 
 RESTART: C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day9_阶乘(递归方式).py 
请输入一个正整数:666
666 的阶乘是;1010632056840781493390822708129876451757582398324145411340420807357413802103697022989202806801491012040989802203557527039339704057130729302834542423840165856428740661530297972410682828699397176884342513509493787480774903493389255262878341761883261899426484944657161693131380311117619573051526423320389641805410816067607893067483259816815364609828668662748110385603657973284604842078094141556427708745345100598829488472505949071967727270911965060885209294340665506480226426083357901503097781140832497013738079112777615719116203317542199999489227144752667085796752482688850461263732284539176142365823973696764537603278769322286708855475069835681643710846140569769330065775414413083501043659572299454446517242824002140555140464296291001901438414675730552964914569269734038500764140551143642836128613304734147348086095123859660926788460671181469216252213374650499557831741950594827147225699896414088694251261045196672567495532228826719381606116974003112642111561332573503212960729711781993903877416394381718464765527575014252129040283236963922624344456975024058167368431809068544577258472983979437818072648213608650098749369761056961203791265363665664696802245199962040041544438210327210476982203348458596093079296569561267409473914124132102055811493736199668788534872321705360511305248710796441479213354542583576076596250213454667968837996023273163069094700429467106663925419581193136339860545658673623955231932399404809404108767232000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
>>> 
 RESTART: C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day9_小兔崽子.py 
Traceback (most recent call last):
  File "C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day9_小兔崽子.py", line 20, in <module>
    if sesult != -1:
NameError: name 'sesult' is not defined
>>> 
 RESTART: C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day9_小兔崽子.py 
Traceback (most recent call last):
  File "C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day9_小兔崽子.py", line 20, in <module>
    if sesult != -1:
NameError: name 'sesult' is not defined
>>> 
 RESTART: C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day9_小兔崽子.py 
Traceback (most recent call last):
  File "C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day9_小兔崽子.py", line 20, in <module>
    if sesult != -1:
NameError: name 'sesult' is not defined
>>> 
 RESTART: C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day9_小兔崽子.py 
总共有6765对小兔崽子诞生
>>> 
 RESTART: C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day9_小兔崽子.py 
总共有1548008755920对小兔崽子诞生
>>> 
 RESTART: C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day9_小兔崽子(递归).py 
总共有%d对小兔崽子诞生 6765
>>> 
 RESTART: C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day9_小兔崽子(递归).py 
