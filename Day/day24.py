Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from io import StringIO
>>> f = StringIO()
>>> f.writ('hello')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    f.writ('hello')
AttributeError: '_io.StringIO' object has no attribute 'writ'
>>> f.write('hello')
5
>>> f.write('h')
1
>>> f.write('')
0
>>> f.write(' ')
1
>>> f.getvalue()
'helloh '
>>> print(f.getvalue())
helloh 
>>> from io import StringIO
>>> f = StringIO('Hello!\nhi!\nGoodbyebye!')
>>> while True:
	s = f.readline()
	if s== '':
		break
	print(s.strip())

	
Hello!
hi!
Goodbyebye!
>>> from io import BytesIO
>>> f = BytesIO()
>>> f.write('中文'.encode('utf-8'))
6
>>> print(f.getvalue())
b'\xe4\xb8\xad\xe6\x96\x87'
>>> form io import BytesIO
SyntaxError: invalid syntax
>>> from io import BytesIO
>>> f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
>>> f.read()
b'\xe4\xb8\xad\xe6\x96\x87'
>>> import os
>>> os.name
'nt'
>>> os.uname()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    os.uname()
AttributeError: module 'os' has no attribute 'uname'
>>> os.uname()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    os.uname()
AttributeError: module 'os' has no attribute 'uname'
>>> impost os
SyntaxError: invalid syntax
>>> import os
>>> os.uname()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    os.uname()
AttributeError: module 'os' has no attribute 'uname'
>>> os.environ
environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\JK-chenxs\\AppData\\Roaming', 'COMMONPROGRAMFILES': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'LILILILILILI', 'COMSPEC': 'C:\\Windows\\system32\\cmd.exe', 'FP_NO_HOST_CHECK': 'NO', 'HOME': 'C:\\Users\\JK-chenxs', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\JK-chenxs', 'LOCALAPPDATA': 'C:\\Users\\JK-chenxs\\AppData\\Local', 'LOGONSERVER': '\\\\LILILILILILI', 'NUMBER_OF_PROCESSORS': '8', 'NVIDIAWHITELISTED': '0x01', 'OS': 'Windows_NT', 'PATH': 'C:\\Program Files\\Common Files\\Microsoft Shared\\Windows Live;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;E:\\wamp64\\bin\\php\\php7.0.10;E:\\wamp64\\bin\\php\\php7.0.10;F:\\Git\\cmd;C:\\Program Files\\Intel\\WiFi\\bin\\;C:\\Program Files\\Common Files\\Intel\\WirelessCommon\\;C:\\Users\\JK-chenxs\\AppData\\Local\\Programs\\Python\\Python36-32;C:\\composer;C:\\ProgramData\\ComposerSetup\\bin;C:\\Users\\JK-chenxs\\AppData\\Local\\Programs\\Python\\Python36-32\\Scripts\\;C:\\Users\\JK-chenxs\\AppData\\Local\\Programs\\Python\\Python36-32\\;C:\\Program Files\\Common Files\\Microsoft Shared\\Windows Live;C:\\Users\\JK-chenxs\\AppData\\Roaming\\Composer\\vendor\\bin;C:\\Program Files\\Intel\\WiFi\\bin\\;C:\\Program Files\\Common Files\\Intel\\WirelessCommon\\', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 'PROCESSOR_ARCHITECTURE': 'x86', 'PROCESSOR_ARCHITEW6432': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 60 Stepping 3, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '3c03', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files (x86)', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PSMODULEPATH': 'C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules\\', 'PUBLIC': 'C:\\Users\\Public', 'SESSIONNAME': 'Console', 'SHIM_MCCOMPAT': '0x810000001', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\Windows', 'TEMP': 'C:\\Users\\JK-CHE~1\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\JK-CHE~1\\AppData\\Local\\Temp', 'USERDOMAIN': 'LILILILILILI', 'USERNAME': 'JK-chenxs', 'USERPROFILE': 'C:\\Users\\JK-chenxs', 'VBOX_MSI_INSTALL_PATH': 'D:\\oracle\\', 'WINDIR': 'C:\\Windows', 'WINDOWS_TRACING_FLAGS': '3', 'WINDOWS_TRACING_LOGFILE': 'C:\\BVTBin\\Tests\\installpackage\\csilogfile.log'})
>>> os.environ.get('PATH')
'C:\\Program Files\\Common Files\\Microsoft Shared\\Windows Live;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;E:\\wamp64\\bin\\php\\php7.0.10;E:\\wamp64\\bin\\php\\php7.0.10;F:\\Git\\cmd;C:\\Program Files\\Intel\\WiFi\\bin\\;C:\\Program Files\\Common Files\\Intel\\WirelessCommon\\;C:\\Users\\JK-chenxs\\AppData\\Local\\Programs\\Python\\Python36-32;C:\\composer;C:\\ProgramData\\ComposerSetup\\bin;C:\\Users\\JK-chenxs\\AppData\\Local\\Programs\\Python\\Python36-32\\Scripts\\;C:\\Users\\JK-chenxs\\AppData\\Local\\Programs\\Python\\Python36-32\\;C:\\Program Files\\Common Files\\Microsoft Shared\\Windows Live;C:\\Users\\JK-chenxs\\AppData\\Roaming\\Composer\\vendor\\bin;C:\\Program Files\\Intel\\WiFi\\bin\\;C:\\Program Files\\Common Files\\Intel\\WirelessCommon\\'
>>> oi.environ.get('x', 'default')
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    oi.environ.get('x', 'default')
NameError: name 'oi' is not defined
>>> os.environ.get('x', 'default')
'default'
>>> os.path.abspath('.')
'C:\\Users\\JK-chenxs\\AppData\\Local\\Programs\\Python\\Python36-32'
>>> os.path.join('C:\\Users\\JK-chenxs\\AppData\\Local\\Programs\\Python\\Python36-32', 'testdir')
'C:\\Users\\JK-chenxs\\AppData\\Local\\Programs\\Python\\Python36-32\\testdir'
>>> os.mkdir('C:\\Users\\JK-chenxs\\AppData\\Local\\Programs\\Python\\Python36-32\\testdir')
>>> os.rmdir('C:\\Users\\JK-chenxs\\AppData\\Local\\Programs\\Python\\Python36-32\\testdir')
>>> os.path.split('C:\\Users\\JK-chenxs\\AppData\\Local\\Programs\\Python\\Python36-32\\testdir\\file.txt')
('C:\\Users\\JK-chenxs\\AppData\\Local\\Programs\\Python\\Python36-32\\testdir', 'file.txt')
>>> os.path.splitext('C:\Users\JK-chenxs\AppData\Local\Programs\Python\Python36-32\Day\day.1py')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> 
