class Student(object):
    count = 0
    count1 = [0]
    def init(self, name):
        self.name = name
        Student.count += 1
        self.count +=1
        Student.count1[0] += 1
        self.count1[0] += 1

if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')
a=Student('a')
b=Student('b')
print(Student.count,Student.count1)



##我是一个有问题的示例
