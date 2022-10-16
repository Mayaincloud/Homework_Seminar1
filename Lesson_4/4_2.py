# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0,
#    с помощью дополнительных библиотек python. Запросите значения А, В, С 3 раза.
#    Уравнения и корни запишите в файл.

from math import sqrt

def abc(a, b, c):
    dis = b**2 - (4 * a * c)
    with open('result.txt', 'a', encoding='utf-8') as my_f:
        my_f.write(f"{a}X^2 + {b}x + {c} = 0\n")
        if dis > 0:
            my_f.write(str((-b + sqrt(dis)) / (2 * a)) + '\n')
            my_f.write(str((-b - sqrt(dis)) / (2 * a)) + '\n')
        elif dis == 0:
            my_f.write(str(-b / (2 * a)) + '\n')
        else:
            my_f.write('Корней нет' + '\n')

abc(1, 2, -3)
