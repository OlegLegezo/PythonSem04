# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:

# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python


path = 'PythonSem04/ex_03_v2/file.txt'

with open(path, 'r') as f:
    a = int(f.readline())
    b = int(f.readline())
    c = int(f.readline())

disc = b**2 - 4 * a * c
x1 = -b + (disc**(1/2) / (2 * a))
x2 = -b - (disc**(1/2) / (2 * a))
print(x1, x2)

with open(path, 'a') as f:
    f.write(f'\nКорень 1: {x1}')
    f.write(f'\nКорень 2: {x2}')