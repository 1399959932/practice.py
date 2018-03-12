f = open('C:\\Users\\JK-chenxs\\AppData\\Local\\Programs\\Python\\Python36-32\\Day\\day11record.txt')

man = []
woman = []
count = 1

for each_line in f:
    if each_line[:6] != '======':
        #我们这里进行字符串分割操作
        (role, line_spoken) = each_line.split(':', 1)
        if role == 'boy':
            man.append(line_spoken)
        if role == 'girl':
            woman.append(line_spoken)
    else:
        #我们这里进行文件的分别保存操作
        file_name_man = 'man_' + str(count) + '.txt'
        file_name_woman = 'woman_' + str(count) + '.txt'

        man_file = open(file_name_man, 'w')
        woman_file = open(file_name_woman, 'w')

        man_file.writelines(man)
        woman_file.writelines(woman)

        man_file.close()
        woman_file.close()
        
        boy = []
        girl = []
        count +=1

file_name_man = 'man_' + str(count) + '.txt'
file_name_woman = 'woman_' + str(count) + '.txt'

man_file = open(file_name_man, 'w')
woman_file = open(file_name_woman, 'w')

man_file.writelines(man)
woman_file.writelines(woman)

man_file.close()
woman_file.close()


f.close()
