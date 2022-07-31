
import os

# path = 'folder'+os.sep+'file.txt'
path = os.path.join('PythonSem04','ex_01','folder', 'file.txt')
# print(path)
# w - заменить+создать+пересоздать (полностью пересоздаст, удалив прошлую инфу)
# a - дописать что-то (отккрыть файл и дописать новые)
# r - только прочитать
with open(path, 'r') as f:
    data = f.read(5)
    # в скобке указываем кол-во символов, которые нужно прочитать
    print (data)

    data2 = f.readlines()
    # считает в список
    print (data2)

    data3 = f.readline()
    # считает строку
    print (data3)


path2 = os.path.join('PythonSem04','ex_01','folder', 'file2.txt')
with open(path2, 'w') as data:
    data.write('jdfkjsdjfksdfksdkj\n')
    data.write('jdfkjsdjfksdfksdkj\n')
    print(data.read())
    # 

