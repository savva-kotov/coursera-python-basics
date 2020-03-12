"""
Напишите программу, которая выбирает из полученной последовательности квадраты целых чисел выводит их в обратном порядке. Использовать массив для хранения последовательности не разрешается.

Формат ввода
Во входных строках записаны целые числа, по одному в каждой строке. В последней строке записано число 0.

Формат вывода
Программа должна вывести элементы полученной последовательности, которые представляют собой квадраты целых чисел, в обратном порядке в одну строчку, разделив их пробелами. Если таких нет, программа должна вывести число 0.

Тест 1
Входные данные:
1
2
3
4
0
Вывод программы:
 4 1

Тест 2
Входные данные:
3
5
0
Вывод программы:
0

Тест 3
Входные данные:
777
66883
0
Вывод программы:
0
"""
# 04.09.19
import math as m


def issq(a):
    if a % m.sqrt(a) == 0:
        return True
    else:
        return False


a = int(input())
res = [a]
while a != 0:
    a = int(input())
    res.append(a)
res1 = [i for i in res[:-1] if issq(i) is True][::-1]
if len(res1) == 0:
    print(0)
else:
    print(' '.join(map(str, res1)))