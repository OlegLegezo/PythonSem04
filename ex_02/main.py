# 1. Считать строку из файла. Напишите программу,
#  которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

from ast import In
import os

path = os.path.join('PythonSem04', 'ex_02', 'file.txt')
with open(path, 'r') as f:
    text = f.readline()

# метод для конвертации в инт из строку


def convert_to_int(str):
    return [int(x) for x in str.split()]


int_list = convert_to_int(text)
print(int_list)
print(max(int_list))
print(min(int_list))
