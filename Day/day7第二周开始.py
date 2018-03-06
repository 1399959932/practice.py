Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> import math # 导入math模块，下面用到pi
list1 = [12.34, 9.08, 73.1] # 将3个不同面积的圆半径定义成一个lis

def area_sum(i): # 定义area_sum函数，套用圆的面积计算公式
	area = math.pi * i * i
	print(area) # 打印圆的面积

for i in list1:# 将列表的3个半径循环
	print(i	)  # 一次将值给area_sum函数
	
SyntaxError: multiple statements found while compiling a single statement
>>> import math
>>> list1 = [12, 34, 56]
>>> def area_sum(i):
	area = math.pi * i * i
	print(area)

	
>>> area
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    area
NameError: name 'area' is not defined
>>> area_sum
<function area_sum at 0x0301A2B8>
>>> area
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    area
NameError: name 'area' is not defined
>>> area
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    area
NameError: name 'area' is not defined
>>> for j in list1:
	area_num(j)

	
Traceback (most recent call last):
  File "<pyshell#14>", line 2, in <module>
    area_num(j)
NameError: name 'area_num' is not defined
>>> def area_sum(i):
	area = math.pi * i * i
	print(area)

	
>>> area_sum(list1[2])
9852.03456165759
>>> abs(3.14)
3.14
>>> abs(3.1454668465465456454)
3.1454668465465456
>>> a = abs()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a = abs()
TypeError: abs() takes exactly one argument (0 given)
>>> a = abs
>>> a(456+8)
464
>>> a(-456+8)
448
>>> print(5.1)
5.1
>>> print(int(5.1))
5
>>> print(hex(int(5.1)))
0x5
>>> 
 RESTART: C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day7_1.py 
请输入需要的转换为16进制的数字:4.2
Traceback (most recent call last):
  File "C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day7_1.py", line 1, in <module>
    数字 = int(input("请输入需要的转换为16进制的数字:"))
ValueError: invalid literal for int() with base 10: '4.2'
>>> 
 RESTART: C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day7_1.py 
请输入需要的转换为16进制的数字:4
4 转换为16进制的字符为： 0x4
>>> 
 RESTART: C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day7_1.py 
请输入需要的转换为16进制的数字:16.4
Traceback (most recent call last):
  File "C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day7_1.py", line 1, in <module>
    数字 = int(input("请输入需要的转换为16进制的数字:"))
ValueError: invalid literal for int() with base 10: '16.4'
>>> 
 RESTART: C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day7_1.py 
请输入需要的转换为16进制的数字:5
Traceback (most recent call last):
  File "C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day7_1.py", line 2, in <module>
    print(数字,"转换为16进制的字符为：",hex(数字))
TypeError: 'float' object cannot be interpreted as an integer
>>> 
 RESTART: C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day7_1.py 
请输入需要的转换为16进制的数字:6.2
Traceback (most recent call last):
  File "C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day7_1.py", line 2, in <module>
    print(数字,"转换为16进制的字符为：",hex(数字))
TypeError: 'float' object cannot be interpreted as an integer
>>> 
 RESTART: C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day7_1.py 
请输入需要的转换为16进制的数字:6
6 转换为16进制的字符为： 0x6
>>> 
 RESTART: C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day7_1.py 
请输入需要的转换为16进制的数字:16.2
Traceback (most recent call last):
  File "C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day7_1.py", line 1, in <module>
    i = int(input("请输入需要的转换为16进制的数字:"))
ValueError: invalid literal for int() with base 10: '16.2'
>>> print()

>>> i = 6.14
>>> print(i)
6.14
>>> print(int(i))
6
>>> print(hex(int(i)))
0x6
>>> 
 RESTART: C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day7_1.py 
请输入需要的转换为16进制的数字:6.14
Traceback (most recent call last):
  File "C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day7_1.py", line 2, in <module>
    print(i,"转换为16进制的字符为：",hex(int(i)))
ValueError: invalid literal for int() with base 10: '6.14'
>>> 
 RESTART: C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day7_1.py 
请输入需要的转换为16进制的数字:6
6 转换为16进制的字符为： 0x6
>>> 
 RESTART: C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day7_1.py 
请输入需要的转换为16进制的数字:7.1
Traceback (most recent call last):
  File "C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day7_1.py", line 1, in <module>
    i = int(input("请输入需要的转换为16进制的数字:"))
ValueError: invalid literal for int() with base 10: '7.1'
>>> n1 = hex(255)
n2 = hex(1000)
print('n1的十六进制形式：'+str(n1))
print('n2的十六进制形式：'+str(n2))
SyntaxError: multiple statements found while compiling a single statement
>>> n = 56
>>> nn = 658
>>> a = [int(n1), int(n2)]
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a = [int(n1), int(n2)]
NameError: name 'n1' is not defined
>>> a = [int(nn), int(nn)]
>>> for i in a:
	print(str(hex(x)))

	
Traceback (most recent call last):
  File "<pyshell#39>", line 2, in <module>
    print(str(hex(x)))
NameError: name 'x' is not defined
>>> for i in a:
	print(hex(x))

	
Traceback (most recent call last):
  File "<pyshell#41>", line 2, in <module>
    print(hex(x))
NameError: name 'x' is not defined
>>> a
[658, 658]
>>> for i in a:
	print(hex(x))

	
Traceback (most recent call last):
  File "<pyshell#45>", line 2, in <module>
    print(hex(x))
NameError: name 'x' is not defined
>>> 
 RESTART: C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day7_1.py 
>>> 
>>> 6
6
>>> 
 RESTART: C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day7_1.py 
>>> def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

>>> my_
